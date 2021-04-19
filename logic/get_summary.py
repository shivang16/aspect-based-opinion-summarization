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
    newData['rating'] = data['rating']
    total_upvotes = newData['upvotes'].sum()
    polarities = []
    for index, row in newData.iterrows():
        x = sentiment_analysis.getPolarity(row['original'],row['aspects'])    
        polarities.append(x)    
        for j in row['aspects']:
            aspect_count[j]=aspect_count[j]+1
    # print(aspect_count)
    # print(total_upvotes)
    newData['polarity'] = polarities
    newData.sort_values("upvotes",axis=0,inplace=True,ascending=False)
    # print(newData)
    aspect_rating = {}
    aspect_upvotes = {}
    rating_sum = {}
    for i in selected_aspects:
        aspect_rating[i] = 0
        aspect_upvotes[i] = 0
        rating_sum[i] = 0

    for index, row in newData.iterrows():
        for a,p in row['polarity'].items():
            if str(p) =='Sentiment.negative':
                aspect_rating[a] -=row['upvotes']
            elif str(p) =='Sentiment.positive':
                aspect_rating[a] +=row['upvotes']
            aspect_upvotes[a]+=row['upvotes']
            rating_sum[a]+=row['rating']
    # print(rating_sum)
    rating_average = rating_sum
    for i in selected_aspects:
        rating_average[i] = rating_sum[i]/aspect_count[i]
    # print(rating_average)
    for i in selected_aspects:
        aspect_rating[i]/=aspect_upvotes[i]
        aspect_rating[i]+=1
        aspect_rating[i]*=2
        aspect_rating[i]+=1
    ratings = aspect_rating
    # print(ratings)
    for i in selected_aspects:
        ratings[i] = pow(ratings[i]*rating_average[i],0.5)
    # print(ratings)
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