#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 05:45:25 2020

@author: abhijithneilabraham
"""
from data_utils import data_utils
d=data_utils(['http://abhijithneilabraham.me/eywabot/','http://abhijithneilabraham.me/'])
data=d.read_data(crawl=True)