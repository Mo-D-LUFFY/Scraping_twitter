import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Load tweets from CSV file
def load_tweets_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df['Text'].tolist()  # Focus on the 'Text' column

# Reading text from CSV
tweets = load_tweets_from_csv('C:\\Users\\ayush\\Downloads\\tempCSV.csv')
text = " ".join(tweets)

# Converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Splitting text into words
tokenized_words = cleaned_text.split()

# Define stop words
stop_words = set([...])  # Add your stop words here

# Removing stop words from the tokenized words list
# Removing stop words and handling frequencies
final_words = [word for word in tokenized_words if word not in stop_words]

# Get emotions text with word frequency
emotion_list = []
emotion_word_freq = Counter()
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
            emotion_word_freq[emotion] += 1

# Count emotions and plot frequencies
w = emotion_word_freq

# Plotting code remains the same
fig, ax1 = plt.subplots(figsize=(12, 8))
colors = cm.viridis(range(len(w)))
ax1.barh(list(w.keys()), list(w.values()), color=colors)
for i, v in enumerate(w.values()):
    ax1.text(v + 1, i, str(v), color='black', va='center', fontsize=12)
plt.title('Emotions from Tweets (With Word Frequencies)', fontsize=16)
plt.xlabel('Counts', fontsize=14)
plt.ylabel('Emotions', fontsize=14)
plt.savefig('detailed_sentiment_graph_with_frequencies.png')
plt.show()
