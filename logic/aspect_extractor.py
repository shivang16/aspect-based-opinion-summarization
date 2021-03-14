import spacy as spacy
import nltk
import pandas as pd


nlpExtractor = spacy.load("en_core_web_sm")

def extract_aspects(text):
    doc = nlpExtractor(text)
    # You want list of Verb tokens 
    aspects = [token.text for token in doc if token.pos_ == "NOUN"]
    return aspects

def final_aspects(data,top_N):
    word_list = []
    for index, row in data.iterrows():
        word_list += row['aspects']
    word_list
    word_dist = nltk.FreqDist(word_list)
    topN_words = pd.DataFrame(word_dist.most_common(top_N),columns=['Word', 'Frequency'])
    return topN_words;