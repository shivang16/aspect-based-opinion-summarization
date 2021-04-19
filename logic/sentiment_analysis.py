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
    sum = 0
    for index, row in data.head(n).iterrows():
        aspects_output = absaNLP(row[column],aspects=selected_aspects)
        sum+=pow(row['upvotes'],0.2)  
        for i in range(len(selected_aspects)):  
            temp1 = aspects_output.subtasks[selected_aspects[i]].examples[0].scores
            x = [k*pow(row['upvotes'],0.2) for k in temp1]
            aspects_score[selected_aspects[i]] = list(map(add, aspects_score[selected_aspects[i]], x))
    for i in range(len(selected_aspects)):    
        temp = aspects_score[selected_aspects[i]]
        aspects_score[selected_aspects[i]] = [m/(sum) for m in temp]
    return aspects_score

def getPolarity(sentence,aspect):
    if len(aspect)==0:
        return {}
    aspects_output = absaNLP(sentence,aspects=aspect)
    output = {}
    for i in aspect:
        output[i] = aspects_output.subtasks[i].examples[0].sentiment
    return output