# -*- coding: utf-8 -*-
"""btp_part2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QNvtveUg3bEohujIOGS3957v2M3xiGhx
"""

!pip install text2emotion
!pip uninstall emoji -y
!pip install emoji==0.6.0
!pip install textblob nltk

from textblob import TextBlob
import matplotlib.pyplot as plt

# Function to perform sentiment analysis using TextBlob
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Function to perform emotion analysis using the NRC lexicon
def perform_emotion_analysis(text):
    emotion_categories = {
        'anger': 0,
        'anticipation': 0,
        'disgust': 0,
        'fear': 0,
        'joy': 0,
        'negative': 0,
        'positive': 0,
        'sadness': 0,
        'surprise': 0,
        'trust': 0
    }

    # Load NRC lexicon
    lexicon_path = 'NRC-Emotion-Lexicon-Wordlevel-v0.92.txt'
    with open(lexicon_path, 'r') as file:
        lines = file.readlines()
        word_emotion_map = {}
        for line in lines:
            word, emotion, value = line.strip().split('\t')
            if word not in word_emotion_map:
                word_emotion_map[word] = {}
            word_emotion_map[word][emotion] = int(value)

    words = text.lower().split()
    for word in words:
        if word in word_emotion_map:
            for emotion in emotion_categories.keys():
                emotion_categories[emotion] += word_emotion_map[word].get(emotion, 0)

    return emotion_categories

# Read text from a local file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# File path of the text file
file_path = 'Jessica - Original.txt'

# Read text from the file
sample_text = read_text_file(file_path)

# Perform sentiment analysis
sentiment_polarity, sentiment_subjectivity = perform_sentiment_analysis(sample_text)
print("Sentiment Analysis Scores (TextBlob):")
print(f"Polarity: {sentiment_polarity}, Subjectivity: {sentiment_subjectivity}")

# Perform emotion analysis
emotion_scores = perform_emotion_analysis(sample_text)
print("\nEmotion Analysis Scores (NRC lexicon):")
print(emotion_scores)


# Plotting Sentiment Analysis Scores
sentiment_labels = ['Polarity', 'Subjectivity']
sentiment_scores = [sentiment_polarity, sentiment_subjectivity]

plt.figure(figsize=(8, 6))
plt.bar(sentiment_labels, sentiment_scores, color=['skyblue', 'lightgreen'])
plt.title('Sentiment Analysis Scores')
plt.ylabel('Score')
plt.show()


# Plotting Emotion Analysis Scores
emotions = list(emotion_scores.keys())
scores = list(emotion_scores.values())

plt.figure(figsize=(10, 6))
plt.bar(emotions, scores, color='lightblue')
plt.title('Emotion Analysis Scores')
plt.ylabel('Frequency')
plt.xlabel('Emotion')
plt.xticks(rotation=45)
plt.show()