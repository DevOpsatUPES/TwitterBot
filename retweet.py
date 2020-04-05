import tweepy
import time
from configapi import init_api
'''
# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXXXX", "XXXXXX")
auth.set_access_token("XXXXXX", "XXXXXX")
'''
# Create API object
api = init_api()
'''
#Handling Errors while verifying credentials
try:
    api.verify_credentials()
    print("Authetication Successful")
except:
    print("Authentication Failure")
'''
# Create a Test tweet
#api.update_status("Test Tweet for Bot")

#Retweet Reply for #DevOpsatUPES 
for tweet in tweepy.Cursor(api.search,q='#DevOpsatUPES'):
    try:
        print("\n RT by Bot")
        tweet.retweet()
        api.update_status('@' +  tweet.user.screen_name + "Cheers!", tweet.id)

        print("RT & Reply Success!")
        time.sleep(5) #sleep for 5 seconds before next RT
    except:
        print("Failure!")