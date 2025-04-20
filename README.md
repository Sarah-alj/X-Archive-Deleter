# X-Archive-Deleter

# 🧹 Script

A simple Python script to delete tweets, retweets, quote tweets, and replies from your Twitter archive based on year. Perfect for cleaning up your old posts without touching likes or newer tweets.

## 📌 Features
- Deletes tweets only from **2019, 2020, and 2021**
- Keeps everything from 2022 and newer
- Supports tweets, replies, retweets, and quote tweets
- Skips likes entirely
- Uses your personal Twitter archive and the official Twitter API

## 🛠️ Requirements

- Python 3.x
- Tweepy:  
  Install with:
  ```bash
  pip install tweepy
  
🚀 How to Use

    Download your Twitter archive and extract tweets.js

    Clone this repo or download delete_old_tweets.py

    Place tweets.js in the same folder as the script

    Set up a Twitter Developer App

        Make sure it has Read and Write permissions

        Get your API Key, API Secret, Access Token, and Access Token Secret

    Open delete_old_tweets.py and paste your keys

    Run the script:

    python delete_old_tweets.py

🔐 Important Notes

    This script uses OAuth 1.0a (via Tweepy)

    It will only delete your own tweets and nothing else

    Do not share your credentials

    Likes and content from 2022+ will be untouched


📄 License

MIT License – feel free to fork and modify it for your own cleanup!
