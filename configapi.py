import tweepy
import logging
import os

log = logging.getLogger()

def init_api():
    consumerkey = os.getenv("X")
    consumersecret = os.getenv("X")
    accesstoken = os.getenv("X")
    accesstokensecret = os.getenv("X")

    auth = tweepy.OAuthHandler(consumerkey,consumersecret)
    auth.set_access_token(accesstoken,accesstokensecret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as ex :
        logger.error("Error in API")
        raise ex
    logger.info("API Success!")
    return api