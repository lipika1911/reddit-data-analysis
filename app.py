import streamlit as st
import praw
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

# Streamlit App
st.title('Reddit Analysis App')

# Input for subreddit
subreddit_name = st.text_input('Enter Subreddit Name', 'learnpython')

if subreddit_name:
    # Fetch the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Display subreddit information
    st.write(f'Subreddit: {subreddit.display_name}')
    st.write(f'Description: {subreddit.public_description}')
    st.write(f'Subscribers: {subreddit.subscribers}')

    # Fetch top posts
    top_posts = subreddit.top(limit=50)  # Increase limit for more data
    posts_data = []
    sentiments = []
    for post in top_posts:
        # Analyze sentiment
        blob = TextBlob(post.title)
        sentiment = blob.sentiment.polarity
        
        posts_data.append({
            'Title': post.title,
            'Score': post.score,
            'Comments': post.num_comments,
            'Upvote Ratio': post.upvote_ratio,
            'Created': pd.to_datetime(post.created_utc, unit='s'),  # Convert timestamp to datetime
            'Sentiment Polarity': sentiment,
        })
        sentiments.append(sentiment)

    # Create DataFrame
    df = pd.DataFrame(posts_data)
    st.write(df)

    # Calculate Metrics
    df['Engagement Rate'] = df['Score'] + df['Comments']  # Simple metric combining score and comments
    df['Comment-to-Upvote Ratio'] = df['Comments'] / (df['Score'] + 1)  # Avoid division by zero

    st.write(f"Average Score: {df['Score'].mean()}")
    st.write(f"Average Comments: {df['Comments'].mean()}")
    st.write(f"Average Upvote Ratio: {df['Upvote Ratio'].mean():.2f}")
    st.write(f"Average Engagement Rate: {df['Engagement Rate'].mean()}")
    st.write(f"Average Comment-to-Upvote Ratio: {df['Comment-to-Upvote Ratio'].mean():.2f}")
    st.write(f"Average Sentiment Polarity: {pd.Series(sentiments).mean():.2f}")

    # Visualize Data
    fig, ax = plt.subplots(figsize=(10, 5))
    df.plot(x='Created', y='Score', kind='line', ax=ax, marker='o', color='b', title='Score Over Time')
    plt.xlabel('Date')
    plt.ylabel('Score')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    df.plot(x='Created', y='Comments', kind='bar', ax=ax, color='r', title='Comments Over Time')
    plt.xlabel('Date')
    plt.ylabel('Comments')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    df['Engagement Rate'].plot(kind='hist', bins=30, ax=ax, color='g', title='Distribution of Engagement Rate')
    plt.xlabel('Engagement Rate')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    df['Sentiment Polarity'].plot(kind='hist', bins=30, ax=ax, color='purple', title='Distribution of Sentiment Polarity')
    plt.xlabel('Sentiment Polarity')
    st.pyplot(fig)

    # Recommendations
    avg_engagement_rate = df['Engagement Rate'].mean()
    avg_sentiment_polarity = df['Sentiment Polarity'].mean()

    st.write("### Recommendations")
    if avg_engagement_rate > df['Engagement Rate'].median():
        st.write("Posts are engaging well. Consider increasing posting frequency.")
    else:
        st.write("Posts are less engaging. Review content quality and posting times.")

    if avg_sentiment_polarity > 0:
        st.write("Overall sentiment is positive. Continue creating similar content.")
    else:
        st.write("Overall sentiment is negative. Consider reviewing and adjusting your content strategy.")

    # Option to download data
    st.download_button(
        label='Download CSV',
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='reddit_top_posts_extended_analysis.csv',
        mime='text/csv'
    )
