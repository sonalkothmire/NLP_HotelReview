import streamlit as st
import pickle
import numpy as np
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained models
kmeans = pickle.load(open("kmeans_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# App title
st.title("TripAdvisor Review Clustering & Sentiment App")

# User input
review = st.text_area("Enter a customer review:")

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        # Clean and transform review
        review_clean = review.lower()
        review_tfidf = tfidf.transform([review_clean])

        # Predict cluster
        cluster = kmeans.predict(review_tfidf)[0]
        st.subheader(f"Predicted Cluster: {cluster}")

        # Sentiment analysis using TextBlob
        sentiment_score = TextBlob(review).sentiment.polarity
        st.write(f"Sentiment Score: {sentiment_score:.2f}")

        # Interpret sentiment
        if sentiment_score > 0.05:
            st.success("Sentiment: Positive 😊")
        elif sentiment_score < -0.05:
            st.error("Sentiment: Negative 😠")
        else:
            st.warning("Sentiment: Neutral 😐")
