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
    def del_dump(self,filepath): #if json dump exists, remove the dump
        if os.path.isfile(filepath):
            os.remove(filepath)
            
    def create_json_dump(self,filepath,data): #create a json dump with given data mappings
        self.del_dump(filepath)
        with open(filepath, "w") as write_file:
            json.dump(data, write_file)
    def kwd_dump(self):
        url_maps={}
        for url in self.urls:
            url_maps[url]=crawler.crawl(url)
            self.create_json_dump('url_maps.json', url_maps)

    def read_data(self,crawl=False):
        if crawl:
            self.kwd_dump()
            return self.read_data(crawl=False)
        if os.path.isfile('url_maps.json'):
            with open('url_maps.json') as f:
                data=json.load(f)
            df=pd.DataFrame(data)
            return df
        else:
            return self.read_data(crawl=True)

d=data_utils(['http://abhijithneilabraham.me/eywabot/','http://abhijithneilabraham.me/'])
data=d.read_data()
            
    
    
