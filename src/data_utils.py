# # #!/usr/bin/env python3
# # # -*- coding: utf-8 -*-
# # """
# # Created on Tue Sep 29 02:33:31 2020

# # @author: abhijithneilabraham
# # """

from crawler import Crawler
import os
import json
import pandas as pd
crawler=Crawler()
class data_utils:
    def __init__(self,urls):
        self.urls=urls
    def del_dump(self,filepath): #if data dump exists, remove the dump
        if os.path.isfile(filepath):
            os.remove(filepath)          
    def create_df_dump(self,filepath,data): #create a df dump with given data mappings
        self.del_dump(filepath)
        df=pd.DataFrame(data)
        df.to_csv(filepath)
    def data_dump(self): #create data mappings and then dump
        url_maps={'url':[],'bag_of_words':[],'traffic':[]}
        for url in self.urls:
            url_maps['url']+=[url]
            url_maps['bag_of_words']+=crawler.crawl(url)
            url_maps['traffic']+=crawler.get_traffic()
        self.create_df_dump('url_maps.csv', url_maps)

    def read_data(self,crawl=False): #read data, if crawl true then crawl and get data, else use data from  dataset.
        if crawl:
            self.data_dump()
            return self.read_data(crawl=False)
        if os.path.isfile('url_maps.csv'):
            df=pd.read_csv('url_maps.csv')
            return df
        else:
            return self.read_data(crawl=True)


            
    
