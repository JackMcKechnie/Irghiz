import tweepy
import config

def tweet_list(anglis):


    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)

    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET_TOKEN)

    api = tweepy.API(auth)

    api.verify_credentials()

    for angli in anglis:
        api.update_status("New anglicism found: "
                          "\"" + angli[0]  + "\"")
