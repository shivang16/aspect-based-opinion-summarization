import pandas as pd
import os
from logic import make_csv,preprocessing,aspect_extractor,sentiment_analysis

def find_aspects(content):
    make_csv.make_csv(content['reviews'], content['file_name'])
    data = pd.read_csv('./data/original/'+content['file_name']+'.csv')
    data = preprocessing.data_preprocess(data)
    data['preprocessed_header'] = data['header'].apply(
        lambda x: preprocessing.text_preprocess(x))
    # print(data)
    data['preprocessed_text'] = data['text'].apply(
        lambda x: preprocessing.text_preprocess(x))
    # print(data)
    data["final_text"] = data["preprocessed_header"] + ' '+data["preprocessed_text"]

    data['aspects'] = data['final_text'].apply(lambda x:aspect_extractor.extract_aspects(x))
    aspect_list = aspect_extractor.final_aspects(data,20)
    data.to_csv('./data/intermediate/'+content['file_name']+'.csv')
    return aspect_list
    