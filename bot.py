import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("gmnr7Ko7CHjDpN3U7XG7O7B8E", "5E63V14UhWNPHgDcj4KysQ91R1BbMjpzaDaDgiJJo27ePinC8g")
auth.set_access_token("2427185198-0liiBHYMUc9vwmjYwkckw2ZNy7Gu2yzGId0XcQO", "Ri9XxroE4foXfm9c64oaPkFr0frwX4HxWJTXIGPGCHCEY")

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
