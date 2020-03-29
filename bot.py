import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXXXX", "XXXXXX")
auth.set_access_token("XXXXXX", "XXXXXX")

# Create API object
api = tweepy.API(auth)

#Handling Errors while verifying credentials
try:
    api.verify_credentials()
    print("Authetication Successful")
except:
    print("Authentication Failure")

# Create a Test tweet
#api.update_status("Test Tweet for Bot")

#Retweet for #DevOps 
for tweet in tweepy.Cursor(api.search,q='#DevOps').items(3):
    print("\n RT by Bot")
    tweet.retweet()
    print("RT Success!")
    time.sleep(5) #sleep for 5 seconds before next RT
