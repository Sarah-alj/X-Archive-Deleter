import tweepy
import json
from datetime import datetime

# ==== Your Twitter API credentials ====
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'
ACCESS_TOKEN = 'your_access_token_here'
ACCESS_SECRET = 'your_access_secret_here'

# ==== Authenticate ====
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# ==== Load tweets.js ====
with open('tweets.js', 'r', encoding='utf-8') as f:
    content = f.read()
    data = json.loads(content[content.index('=') + 1:])  # remove JS var assignment

# ==== Delete tweets from 2019, 2020, 2021 (skip likes) ====
for tweet in data:
    tweet_id = tweet['tweet']['id']
    created_at = datetime.strptime(tweet['tweet']['created_at'], '%a %b %d %H:%M:%S %z %Y')
    tweet_year = created_at.year

    # Only act on tweets from these years
    if tweet_year in [2019, 2020, 2021]:
        try:
            api.destroy_status(tweet_id)
            print(f"✅ Deleted tweet from {tweet_year}: {tweet_id}")
        except tweepy.errors.NotFound:
            print(f"⚠️ Tweet not found (already deleted?): {tweet_id}")
        except tweepy.errors.Forbidden as e:
            print(f"🚫 Forbidden (maybe not your tweet?): {tweet_id}")
        except Exception as e:
            print(f"❌ Error deleting {tweet_id}: {e}")
