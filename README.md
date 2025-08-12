# Stock-Sentiment-Analysis-finBERT

A real-time financial sentiment analysis application that leverages advanced NLP models to analyze market sentiment from Yahoo Finance news articles. Built with Streamlit for an intuitive web interface and powered by FinBERT for accurate financial text classification.

## Live Demo
**[View Live App](https://stock-sentiment-analysis-finbert-9ktar2jnumevfvkdpow9y4.streamlit.app)** 

# # Key Features:

Real-time News Analysis: Fetches the latest news articles from Yahoo Finance RSS feeds
Advanced NLP: Uses FinBERT (Financial BERT) - a domain-specific language model trained on financial texts
Interactive Web Interface: Clean, responsive Streamlit dashboard with sidebar controls
Sentiment Scoring: Generates overall sentiment scores with confidence metrics
Data Visualization: Interactive pie charts showing sentiment distribution
Flexible Filtering: Optional keyword filtering for targeted analysis
Performance Optimized: Model caching for faster subsequent analyses

# # Technical Stack:

Frontend: Streamlit (Python web framework)
NLP Model: ProsusAI/FinBERT (Hugging Face Transformers)
Data Processing: Pandas, FeedParser
Visualization: Matplotlib
Data Source: Yahoo Finance RSS feeds

# # How It Works:

Data Acquisition: Retrieves real-time news articles from Yahoo Finance RSS feeds using the provided stock ticker
Text Processing: Processes article summaries through the FinBERT pipeline
Sentiment Classification: Classifies each article as Positive, Negative, or Neutral with confidence scores
Aggregation: Calculates weighted overall sentiment score based on confidence levels
Visualization: Presents results in an interactive dashboard with data tables and charts

