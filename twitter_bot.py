import tweepy, os
from time import sleep
from termcolor import colored


author = colored("devloped by: khireddine BELKHIRI @khireddine10", "yellow")
desc = colored(""" twitter boot that will, like, retweet, follow 'depends on the configuration',
 any tweet about cybersecurity programming and other topics developed"
""", "blue")

config = {
    like: True,
    retweet: True,
    follow: False,
    query: "#infosec #tryhackme #hackthebox #cybersecurity #programming #python #hacking",
    time_to_sleep: 400
}

creds = {
    key: os.getenv("TWITTER_KEY"),
    sercret: os.getenv("TWITTER_SECRET"),
    access_token: os.getenv("TWITTER_ATOKEN"),
    secret_token: os.getenv("TWITTER_STOKEN")
}

auth = tweepy.OAuthHandler(creds.key, creds.secret)
auth.set_access_token(creds.access_token, creds.secret_token)
api = tweepy.API(auth)

print(desc)
print(author)

for tweet in tweepy.Cursor(api.search, q=config.query, include_entities=True,
                           monitor_rate_limit=True,
                           wait_on_rate_limit=True).items():
    try:
        # check if retweet the tweet is true in the configuration
        if config.retweet:
            print("Tweet at: \n", tweet.created_at)
            print('Tweet by: @\n' + tweet.user.screen_name)
            print('Tweet Text: \n' + tweet.text)
            tweet.retweet()
            print('The twitte is retweeted\n')
            print('----------------------------------')
        
        # check if like the tweet is true in the configuration
        if config.like:
            tweet.favorite()
            print('The twitte is liked\n')

        # check if follow the user who tweeted is true in the configuration
        # check our boot if it's already following the user
        if config.follow:
            if not tweet.user.following:
                tweet.user.follow()
                print('Following the user who tweeted')

        sleep(config.time_to_sleep)

    except tweepy.TweepError as error:
        print(error.reason)

    except StopIteration:
        break