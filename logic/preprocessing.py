import pandas as pd
import numpy as np
import seaborn as sns
import os
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
import re
import string
from textblob import TextBlob

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


stop_words = list(get_stop_words('en'))
nltk_words = list(stopwords.words('english'))
stop_words.extend(nltk_words)
lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.ADJ)


def text_preprocess(text):
    if text == '':
        return text
    url_pattern = re.compile(r'https?://\S+|www\.\S+|@[^\s]+')
    text = url_pattern.sub(r'', text)
#     print("URL removed")

    text = re.sub('[^A-Za-z]+', ' ', text)
#     print("Puncutation and numbers removed")

    word_tokens = word_tokenize(text)
#     print("Tokenized words")

    filtered_sentence = [w for w in word_tokens if not w in stop_words]
#     print("Stop words removed")

    # Remove numbers
    cleaned_data_title = [
        word for word in filtered_sentence if not word.isnumeric()]
#     print("Remove numbers")

    lemmatized_output = [lemmatizer.lemmatize(
        w, get_wordnet_pos(w)) for w in cleaned_data_title]
#     print("POS lemmatizer")

    # Remove characters which have length less than 2
    without_single_chr = [word for word in lemmatized_output if len(word) > 2]
#     print("Length less than 2 removed")

    final_text = ' '.join(without_single_chr)
    return final_text


def data_preprocess(data):

    data['text'].fillna("There is a book on the desk.", inplace=True)
    data['header'].fillna("There is a book on the desk.", inplace=True)

    data['upvotes'].fillna('0', inplace=True)
    data['rating'].fillna('3', inplace=True)

    data["upvotes"] = data["upvotes"].apply(
        lambda x: int(str(x).replace(',', '')))
    data["rating"] = data["rating"].apply(
        lambda x: int(str(x).replace(',', '')))

    data['upvotes'].fillna(data['upvotes'].mean(), inplace=True)
    data['rating'].fillna(data['rating'].mean(), inplace=True)

    return data
