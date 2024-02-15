import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import data_scraper

# pre process the text by removing certain words and grouping
def preprocess_text(text):
    tokens = word_tokenize(text.lower())

    filtered_tokens = [token for token in tokens if token not in stopwords.words("english")]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    processed_text = " ".join(lemmatized_tokens)
    return processed_text

# add a new column that calculates the sentiment of each line
def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores["pos"] > 0 else 0
    return sentiment

def main():
    df = data_scraper.reddit_top_day()

    df["title"] = df["title"].apply(preprocess_text)

    df["sentiment"] = df["title"].apply(get_sentiment)

    # filter out any lines that have less than 1 sentiment
    df = df[df["sentiment"] == 1]

    return df