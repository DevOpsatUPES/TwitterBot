# Importing python libraries
import tweepy
import time

# Setting the user authorisation keys
CONSUMER_KEY = '*****'
CONSUMER_SECRET = '*****'
ACCESS_KEY = '*****'
ACCESS_SECRET = '*****'

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
    # Waiting for some time so that twitter limit doesn't get exceeded
    time.sleep(150)
    for tweet in api.search(q='#DevOpsatUPES', rpp=15):
    # Checking for tweets containing the hashtag 100DaysOfCodeatUPES
        try:
            print("Searching for posts")
            tweet.retweet()
            # Retweeting the tweet
            api.update_status('@' + tweet.user.screen_name + 'Great times commiting at DevOpsatUPES!', tweet.id)
            # Commenting on the tweet
            api.create_favorite(tweet.id)
            # Liking the tweet
            print("Retweet Succesfull")
        except:
            # Executes in case no post was found
            print("Retweet failed")
