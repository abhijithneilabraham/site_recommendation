
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
    def __init__(self,urls,crawl=False,m=30):
        self.urls=urls
        self.crawl=crawl
        data_process=data_utils(self.urls)
        self.df=data_process.read_data(crawl=self.crawl)
        self.t_avg=self.df['traffic'].mean()
        self.wt=1/self.t_avg
        self.ws=.8
    def get_cosine_similarity(self): #get cosine similarity by getting a count_matrix of n*n shape
        count = CountVectorizer()
        count_matrix = count.fit_transform(self.df['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        return cosine_sim

    def weighted_rating(self,x): #using weights for calculating the overall weighted sum to score
        t= x['traffic']
        s = x['scores']
        w1=self.wt
        w2=self.ws
        weight_sum=(w1*t)+(w2*s)
        return weight_sum
    def recommend(self,url ,num=10): #recommendation engine which uses cosine similarity to sort the most scored links
        cosine_sim=self.get_cosine_similarity()
        indices = pd.Series(self.df['url'])
        idx = indices[indices == url].index[0]
        score_series = pd.Series(cosine_sim[idx])
        self.df['scores']=score_series
        self.df['weighted_scores'] = self.df.apply(self.weighted_rating, axis=1)
        score_weighted_series = self.df.sort_values('weighted_scores', ascending=False)
        print(score_weighted_series[["weighted_scores","url"]])
        top_indices=list(score_weighted_series.index)
        data=list(self.df['url'])
        top_n=[]
        for i,j in enumerate(top_indices):
            if j!=idx:
                top_n.append(data[j])
            if len(top_n)==num:
                break
            
        return top_n
        
        


