
from data_utils import data_utils
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Recommender:
    """
    Arguments:
        urls:list or tuple of urls
        crawl:Default False, set True if crawling needed
    """
    def __init__(self,urls,crawl=False):
        self.urls=urls
        self.crawl=crawl
        data_process=data_utils(self.urls)
        self.df=data_process.read_data(crawl=self.crawl)
    def get_cosine_similarity(self): #get cosine similarity by getting a count_matrix of n*n shape
        count = CountVectorizer()
        count_matrix = count.fit_transform(self.df['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        return cosine_sim
    def recommend(self,url ,num=10): #recommendation engine which uses cosine similarity to sort the most scored links
        cosine_sim=self.get_cosine_similarity()
        recommended_links = []
        indices = pd.Series(self.df['url'])
        idx = indices[indices == url].index[0]
        score_series = pd.Series(cosine_sim[idx])
        print(score_series)
        top_indices = list(score_series.iloc[:num].index)     
        print(top_indices)
        for i in top_indices:
            pred=list(self.df['url'])[i]
            if url!=pred:
                recommended_links.append(list(self.df['url'])[i])
            
        return recommended_links
        
        


