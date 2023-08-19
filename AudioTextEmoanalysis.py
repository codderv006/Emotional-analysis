import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import matplotlib.pyplot as plt
import speech_recognition as sr
from textblob import TextBlob

# Initialize the recognizer
recognizer = sr.Recognizer()

# Record audio from the user
with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source)

# Convert audio to text
try:
    user_input = recognizer.recognize_google(audio)
    print("You said:", user_input)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

# Tokenization, cleaning, and emotion analysis code
text = user_input
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

w = Counter(emotion_list)

# Perform sentiment analysis using TextBlob
def sentiment_analyze(sentiment_text):
    analysis = TextBlob(sentiment_text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        print("Positive Sentiment")
    elif polarity < 0:
        print("Negative Sentiment")
    else:
        print("Neutral Vibe")

sentiment_analyze(cleaned_text)

# Plotting the emotion frequencies as a bar graph
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()
