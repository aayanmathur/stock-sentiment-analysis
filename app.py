import streamlit as st
import feedparser
from transformers import pipeline
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Stock Sentiment Analyzer",
    page_icon="📈",
    layout="wide"
)

# Title & Description
st.title("📈 Stock News Sentiment Analyzer")
st.markdown(
    """
    This app uses **FinBERT** (a financial language model) to analyze sentiment in the latest Yahoo Finance news articles for any stock ticker.  
    Enter a **ticker symbol** (e.g., `BA` for Boeing) and an optional **keyword** to filter results.
    """
)


# Sidebar Inputs
st.sidebar.header("User Input")
ticker = st.sidebar.text_input("Stock Ticker", value="BA").upper()
keyword = st.sidebar.text_input("Keyword (optional)", value="boeing").lower()

analyze_button = st.sidebar.button("Analyze Sentiment")

# FinBERT Pipeline
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="ProsusAI/finbert")

pipe = load_model()

# Function to Get Sentiment
def analyze_sentiment(ticker, keyword):
    rss_url = f'https://finance.yahoo.com/rss/headline?s={ticker}'
    feed = feedparser.parse(rss_url)

    results = []
    score = 0
    num = 0

    for entry in feed.entries:
        if keyword and keyword not in entry.summary.lower():
            continue

        sentiment = pipe(entry.summary)[0]
        label = sentiment['label']
        conf_score = sentiment['score']

        if label == 'positive':
            score += conf_score
            num += 1
        elif label == 'negative':
            score -= conf_score
            num += 1

        results.append({
            "Title": entry.title,
            "Link": entry.link,
            "Published": entry.published,
            "Summary": entry.summary,
            "Sentiment": label.capitalize(),
            "Confidence": round(conf_score, 3)
        })

    final_score = score / num if num > 0 else 0
    if final_score >= 0.15:
        overall_sentiment = "Positive"
    elif final_score <= -0.15:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    return results, overall_sentiment, round(final_score, 3)

# Run Analysis
if analyze_button:
    with st.spinner("Analyzing sentiment..."):
        articles, overall_sentiment, final_score = analyze_sentiment(ticker, keyword)

    if not articles:
        st.warning("No articles found matching your keyword. Try again with a broader keyword or leave it blank.")
    else:
        # Overall Sentiment Display
        st.subheader(f"📊 Overall Sentiment for {ticker}")
        st.markdown(f"**Sentiment:** {overall_sentiment}")
        st.markdown(f"**Score:** {final_score}")

        # DataFrame of Results
        df = pd.DataFrame(articles)
        st.dataframe(df[["Title", "Sentiment", "Confidence", "Published", "Link"]])

        # Sentiment Distribution Chart
        fig, ax = plt.subplots()
        sentiment_counts = df["Sentiment"].value_counts()
        ax.pie(
            sentiment_counts,
            labels=sentiment_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=["#2ecc71", "#e74c3c", "#95a5a6"]
        )
        ax.set_title("Sentiment Distribution")
        st.pyplot(fig)
else:
    st.info("👈 Enter a ticker and click 'Analyze Sentiment' to begin.")
