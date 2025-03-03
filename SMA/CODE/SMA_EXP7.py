import streamlit as st
import tweepy
import pandas as pd
import plotly.express as px
import time
import os
# Replace these with your actual API keys
API_KEY = "jSTNqHt2a3QqXt2d2X2PasV7F"
API_SECRET = "HOV9yCjYIwLf87UWPdMe3q20F6M1nnSatGE1jGH0f2FmQxJJ7j"
ACCESS_TOKEN = "1638646970167296003-VTJAzibKLcggzuhasLrwjPU7EfZjR2"
ACCESS_SECRET = "2qiDq6MiQPvKu1EUrnakdK8xj4r2qV3efnRp5O7ddJuGd"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGkwzgEAAAAAxyOmeDGpO3Zn%2FNvsZ5qMkdPjKcU%3DMoM2vEXxDmimqiY9rj463TuB3ZLFnGIfYbVhdPCPYp9QS1Lmfk"
# Authenticate Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)


def fetch_tweets(query, max_tweets=50):
    tweets = client.search_recent_tweets(query=query, tweet_fields=["created_at", "public_metrics"], max_results=max_tweets)
    data = []
    if tweets.data:
        for tweet in tweets.data:
            data.append({
                "Time": tweet.created_at,
                "Tweet": tweet.text,
                "Likes": tweet.public_metrics["like_count"],
                "Retweets": tweet.public_metrics["retweet_count"],
            })
    return pd.DataFrame(data)


st.title("📸 Twitter Live Dashboard")

# Input Search Query
query = st.text_input("Enter a hashtag or keyword to track:", "#AI")

if st.button("Fetch Tweets"):
    st.write("Fetching latest tweets...")
    df = fetch_tweets(query)
    
    if not df.empty:
        st.write("### Recent Tweets")
        st.dataframe(df)

        # Plot Tweet Engagements
        fig = px.bar(df, x="Time", y=["Likes", "Retweets"], title="Engagement Over Time")
        st.plotly_chart(fig)
    else:
        st.write("No tweets found.")


IMAGE_FOLDER_PATH="images"

def get_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.png', '.jpeg')):  
            images.append(os.path.join(folder_path, filename))
    return images

st.title("📸 Twitter Live Dashboard")

if st.button("Fetch Stats"):
    images = get_images_from_folder(IMAGE_FOLDER_PATH)

    if images:
        images = images[:10]
        
        for i in range(0, len(images), 2):
            cols = st.columns(2)  

            if i < len(images):
                cols[0].image(images[i], width=400) 
            if i + 1 < len(images):
                cols[1].image(images[i + 1], width=400) 
    else:
        st.write("No stats found in the folder.")