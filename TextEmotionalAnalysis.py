# # with help from https://www.youtube.com/watch?v=lcgqP8g6i84&list=PLhTjy8cBISEoOtB5_nwykvB9wfEDscuEo&index=3
# # Cleaning input text

# import string
# from collections import Counter
# import matplotlib.pyplot as plt

# text = open('read.txt', encoding='utf-8').read()
# lower_case = text.lower()
# cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# tokenized_words = cleaned_text.split()
# # print(tokenized_words)
# # as the NLP is analysis of words not the sentences we need tokenization

# # stop words: words that don't add any emotional meaning to the sentence; these can be removed; in NLTK many stop words are predefined
# stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
# final_words = []
# for word in tokenized_words:
#     if word not in stop_words:
#         final_words.append(word)
# # print(final_words)

# # now we can analyze these final words using NLP concepts
# # NLP emotional analysis algo
# # ctrl alt l to format the code
# # 1) Check if the word in the final word list is also present in emotion.txt
# #  - open the emotion file
# #  - Loop through each line and clear it
# #  - Extract the word and emotion using split

# # 2) If word is present -> Add the emotion to emotion_list
# # 3) Finally count each emotion in the emotion list

# emotion_list = []
# with open('emotions.txt', 'r') as file:
#     for line in file:
#         clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
#         word, emotion = clear_line.split(
#             ':')  # to split the emotions.txt and store right side ke words in emotion and left side words in words

#         if word in final_words:
#             emotion_list.append(emotion)
# print(emotion_list)
# w = Counter(emotion_list)
# print(w)

# fig, ax1 = plt.subplots()
# ax1.bar(w.keys(), w.values())
# fig.autofmt_xdate()
# plt.savefig("graph.png")
# plt.show()


# with help from https://www.youtube.com/watch?v=lcgqP8g6i84&list=PLhTjy8cBISEoOtB5_nwykvB9wfEDscuEo&index=3
# Cleaning input text

import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import matplotlib.pyplot as plt

text = open('read1.txt', encoding='utf-8').read()
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
        word, emotion = clear_line.split(
            ':')  # to split the emotions.txt and store right side ke words in emotion and left side words in words

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score["neg"]
    pos = score["pos"]
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibe")

sentiment_analyze(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()
