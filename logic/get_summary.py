import pandas as pd
from logic import sentiment_analysis

def make_summary(content):
    data = pd.read_csv('./data/intermediate/'+content['file_name']+'.csv')
    selected_aspects = content['aspects']
    data["polarity"] = data["final_text"].apply(sentiment_analysis.sentiment)
    aspect_header_score = sentiment_analysis.aspect_sentiment(selected_aspects,data,'preprocessed_header',5)
    aspect_text_score = sentiment_analysis.aspect_sentiment(selected_aspects,data,'preprocessed_text',5)
    return {"header_score":aspect_header_score,"text_score":aspect_text_score}