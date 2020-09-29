
from data_utils import data_utils
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Recommender:
    def __init__(self,urls,crawl=False):
        self.urls=urls
        self.crawl=crawl
        data_process=data_utils(self.urls)
        self.df=data_process.read_data(crawl=self.crawl)
    def get_cosine_similarity(self):
        count = CountVectorizer()
        count_matrix = count.fit_transform(self.df['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        return cosine_sim
    def recommend(self,url ,num=10):
        cosine_sim=self.get_cosine_similarity()
        recommended_links = []
        indices = pd.Series(self.df['url'])
        idx = indices.index[0]
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
        top_indices = list(score_series.iloc[1:num+1].index)     
        for i in top_indices:
            recommended_links.append(list(self.df['url'])[i])
            
        return recommended_links
        
        

