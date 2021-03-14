import aspect_based_sentiment_analysis as absa
from vaderSentiment import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from operator import add 

sent_analyser = SentimentIntensityAnalyzer()
absaNLP = absa.load()

def sentiment(text):
    return (sent_analyser.polarity_scores(text)["compound"])

def aspect_sentiment(selected_aspects,data,column,n):
    aspects_score = {}
    for i in selected_aspects:
        aspects_score[i] = [0,0,0]
    for index, row in data.head(n).iterrows():
        aspects_output = absaNLP(row[column],aspects=selected_aspects)
        for i in range(len(selected_aspects)):    
            aspects_score[selected_aspects[i]] = list(map(add, aspects_score[selected_aspects[i]], aspects_output.subtasks[selected_aspects[i]].examples[0].scores))
    return aspects_score