# Importing python libraries
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import json
import tweepy
import time

# Empty variables for the authorization keys
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

# Empty variable for loading private key of RSA
KEY = ""

# Loading the private key of RSA algorithm
with open('private.pem', mode='r') as f:
    KEY = f.readlines()[0]

# Converting the private key to the desired format and loading it
KEY = KEY[2:-1]
KEY = str(KEY)
KEY = KEY.replace('\\n', '\n')
KEY = RSA.importKey(KEY)

def decrypt(encrypted):
    """
    Accepts the message to be decrypted and decrypts it using the private key

    Arguments : encrypted
    * encrypted - accepts the message to be decrypted
    """
    global KEY
    decrypted = f"{KEY.decrypt(encrypted):08}"
    # print(decrypted)
    return decrypted

def decryptKeys():
    """
    Reads the encrypted messages from the files and decrypt them using the decrypt function and converts the encrypted message to the binary string
    """
    global CONSUMER_KEY
    global CONSUMER_SECRET
    global ACCESS_KEY
    global ACCESS_SECRET
    str_data=''
    with open('consumer.key', mode='r') as f:
        keys = f.read().splitlines()
        for key in keys:
            str_data = str_data + decrypt(int(key))
        CONSUMER_KEY = str_data
    str_data=''
    with open('consumer.secret', mode='r') as f:
        keys = f.read().splitlines()
        for key in keys:
            str_data = str_data + decrypt(int(key))
        CONSUMER_SECRET = str_data
    str_data=''
    with open('access.key', mode='r') as f:
        keys = f.read().splitlines()
        for key in keys:
            str_data = str_data + decrypt(int(key))
        ACCESS_KEY = str_data 
    str_data=''
    with open('access.secret', mode='r') as f:
        keys = f.read().splitlines()
        for key in keys:
            str_data = str_data + decrypt(int(key))
        ACCESS_SECRET = str_data        


def BinaryToDecimal(binary):
    """
    Converts the given binary string to the decimal string

    Arguments : binary
    * binary - accepts the binary string
    """
    string = int(binary, 2)
    return string  	

def convert(bin_data):
    """
    Converts the binary string to decimal string using the BinaryToDecimal function and then converts the decimal string further to character string
    
    Arguments : bin_data
    * bin_data - accepts the binary string
    """
    str_data =''
    for i in range(0, len(bin_data), 8):
        temp_data = bin_data[i:i + 8]
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data) 
    return str_data

# Decrypting the keys
decryptKeys()

# Twitter API keys
CONSUMER_KEY = convert(CONSUMER_KEY)
CONSUMER_SECRET = convert(CONSUMER_SECRET)
ACCESS_KEY = convert(ACCESS_KEY)
ACCESS_SECRET = convert(ACCESS_SECRET)

# Authorising twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creating an API to fetch data from twitter
api = tweepy.API(auth)

# Checking if credentials are verified
try:
    api.verify_credentials()
    print("Authetication Successful")
except:
    print("Authentication Failure")

# Making an infinite loop to iterate over the process of retweeting
while True: 
    for tweet in api.search(q='#100DaysOfCodeatUPES', rpp=15):
    # Checking for tweets containing the hashtag 100DaysOfCodeatUPES
        try:
            print("Searching for posts")
            tweet.retweet()
            # Retweeting the tweet
            api.update_status('@' + tweet.user.screen_name + '#HelloWorld back to you!', tweet.id)
            # Commenting on the tweet
            api.create_favorite(tweet.id)
            # Liking the tweet
            print("Retweet Succesfull")
            # Waiting for two seconds for the next tweet
            time.sleep(2)
        except:
            # Executes in case no post was found
            print("Retweet failed")
