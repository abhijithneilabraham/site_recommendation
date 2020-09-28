# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Sep 29 02:33:31 2020

# @author: abhijithneilabraham
# """

from crawler import Crawler
crawl_urls=['http://abhijithneilabraham.me/eywabot/','https://abhijithneilabraham.github.io/']
crawl=Crawler().crawl
site1='https://abhijithneilabraham.github.io/'
site2='http://abhijithneilabraham.me/eywabot/'
site1_keywords=crawl(site1)
site2_keywords=crawl(site2)
print(len(set(site1_keywords)&set(site2_keywords)))


