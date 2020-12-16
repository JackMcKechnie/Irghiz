import tweepy
import config
import pyshorteners


def tweet_list(anglis):

    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)

    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET_TOKEN)

    api = tweepy.API(auth)

    api.verify_credentials()

    s = pyshorteners.Shortener()
    for angli in anglis:
        url = s.tinyurl.short(angli[1])[8:]
        tweet = "New anglicism found: \"" + angli[0]  + "\". \n" + url
        api.update_status(tweet)

