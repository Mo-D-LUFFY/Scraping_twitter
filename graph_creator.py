import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

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
stop_words = set([...])  # Keep your list of stop words here

# Removing stop words from the tokenized words list
final_words = [word for word in tokenized_words if word not in stop_words]

# Get emotions text
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

# Count emotions
w = Counter(emotion_list)

# Plotting the results
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.title('Emotions from Tweets')
plt.xlabel('Emotions')
plt.ylabel('Counts')
plt.savefig('sentiment_graph.png')
plt.show()
