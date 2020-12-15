import tweepy

def tweet_list(anglis):
    CONSUMER_KEY  = "i1KPnLtsXMLKbeRUw6JYZlkJu"
    CONSUMER_SECRET = "Nl5ZxJIYNbWk07cL4vwmGQcDcHbm28TwDa85b7dpvuT4OE0VbW"
    ACCESS_TOKEN = "1336797900089724931-qDU5TFGwN1AVDhAClDAF8VIn6GqsHX"
    ACCESS_SECRET_TOKEN = "nX6GKippSDtYTlLBhgYITXnxNrYzFWy148ocxfLJnOPlV"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

    api = tweepy.API(auth)

    api.verify_credentials()

    for angli in anglis:
        api.update_status("New anglicism found: "
                          "\"" + angli  + "\"")
