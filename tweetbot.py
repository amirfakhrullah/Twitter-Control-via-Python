import tweepy
from secret import key, key_secret, access_token, access_token_secret


auth = tweepy.OAuthHandler(key, key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#verify 
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#home_timeline() get 20 latest tweets on the timeline
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

#tweet
api.update_status("I just tweeted using Tweepy Python!")

#search users (only public account)
user = api.get_user("Buzzfeed")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

#follow someone
api.create_friendship("kobebryant")

#update profile description
api.update_profile(description="")

#likes the latest tweet on timeline
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

#for blocking user
#to see users that you've blocked
for block in api.blocks():
    print(block.name)

#method for searches
#get 10 most recent public tweets (english) contain word "diego maradona"
for tweet in api.search(q="diego maradona", lang="en", rpp = 10):
    print(f"{tweet.user.name}:{tweet.text}")

#methods for trends
trends_result = api.trends_place(1)
for trends in trends_result[0]["trends"]:
    print(trend["name"])

#likes and follow users that mentioned you
tweets = api.mention_timeline()
for tweet in tweets:
    tweet.favorite()
    tweet.user.follow()


#Cursor: extend pages
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said: {tweet.text}")






