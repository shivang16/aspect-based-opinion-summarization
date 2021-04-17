import pandas as pd
import random as random
import matplotlib.pyplot as plt
import numpy as np
from logic import sentiment_analysis

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    list_set = set(lst3)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list


def Average(lst):
    return sum(lst) / len(lst)

def Convert(string):
    li = list(string.split("', '"))
    return li

def make_summary(content):
    data = pd.read_csv('./data/intermediate/'+content['file_name']+'.csv',converters={'aspects': eval})

    selected_aspects = content['aspects']

    data["polarity"] = data["final_text"].apply(sentiment_analysis.sentiment)
    newData = pd.DataFrame({'original':data['final_text']})
    newData['text'] = data['header']+'. '+data['text']
    temp_aspects = []
    aspect_count = {}

    for i in selected_aspects:
        aspect_count[i] = 0
    for index, row in data.iterrows():
        temp_aspects.append(intersection(row['aspects'],selected_aspects))
    
    newData['aspects'] = temp_aspects
    newData['upvotes'] = data['upvotes']
    polarities = []
    for index, row in newData.iterrows():
        x = sentiment_analysis.getPolarity(row['original'],row['aspects'])    
        polarities.append(x)    
        for j in row['aspects']:
            aspect_count[j]=aspect_count[j]+1
    # print(newData)
    # print(aspect_count)
    
    newData['polarity'] = polarities
    newData.sort_values("upvotes",axis=0,inplace=True,ascending=False)
    aspect_header_score = sentiment_analysis.aspect_sentiment(selected_aspects,data,'preprocessed_header',data.shape[0])
    aspect_text_score = sentiment_analysis.aspect_sentiment(selected_aspects,data,'preprocessed_text',data.shape[0])
    final_score = {}
    for i in selected_aspects:
        final_score[i] = [0,0,0]
    # print(aspect_header_score)
    # print(aspect_text_score)
    for i in selected_aspects:
        for j in range(len(aspect_header_score[i])):
            final_score[i][j] = (3*aspect_header_score[i][j]+2*aspect_text_score[i][j])
    ratings = {}
    for i in selected_aspects:
        ratings[i] = 0
    rating_avg = data['rating'].mean()
    for i in selected_aspects:
        if final_score[i][0]+5-abs(final_score[i][1]-final_score[i][2])>=3.5:
            ratings[i] = 3
        elif final_score[i][1]>=final_score[i][2]:
            ratings[i] = 5-final_score[i][1]
        else:
            ratings[i] = final_score[i][2]
        ratings[i] = pow(ratings[i]*rating_avg,.5)
    rating = {}
    
    for i in selected_aspects:
        if ratings[i]>=3:
            rating[i] = "Sentiment.positive"
        else:
             rating[i] = "Sentiment.negative"
    used = {}
    for i in selected_aspects:
        used[i] = False
    summary_set = set()
    for index, row in newData.iterrows():
        temp_polarity = row['polarity']
        temp_polarity
        for a,p in temp_polarity.items():
            # print(a,p,rating[a],used[a])
            if used[a] == False and rating[a]==str(p):
                used[a] = True
                summary_set.add(row['text'])
            # print(summary_set)
    summary =  ". ".join(summary_set)         
    
    # Creating Pie chart
    PieChartlabels = list(aspect_count.keys())
    PieChartvalues = list(aspect_count.values())
    plt.figure()
    plt.pie(PieChartvalues, labels=PieChartlabels)
    plt.title("Aspects Distribution")
    plt.savefig('./front-end/src/assets/'+'pie-chart-'+content['file_name'])

    # Rating v/s Aspect graph
    l = []
    barX = list(ratings.keys())
    barY = list(ratings.values())
    for i in range(0, len(barX)+1):
        l.append(tuple(np.random.choice(range(0, 2), size=3)))
    plt.figure()
    plt.bar(barX, barY, color =l,width = 0.4)
    plt.ylim(0,6)
    plt.xlabel("Aspects")
    plt.ylabel("Rating")
    plt.title("Aspects vs Out of 5 Rating")
    plt.savefig('./front-end/src/assets/'+'bar-graph-'+content['file_name'])

    final_rating = Average(barY)
    return {"ratings":ratings,"summary":summary,"final_rating":final_rating}