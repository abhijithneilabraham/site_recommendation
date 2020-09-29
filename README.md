# site_recommendation
A recommender system to crawl multiple sites and get recommendation for sites to visit.

`git clone https://github.com/abhijithneilabraham/site_recommendation`.  


`cd src`

```pip install -r requirements.txt```

Example.  
```
from recommender import Recommender
urls=['http://abhijithneilabraham.me/eywabot/','http://abhijithneilabraham.me/','https://abhisharmab.github.io/','https://karuvally.github.io/']
r=Recommender(urls,crawl=True)
res=r.recommend('http://merkle-groot.github.io/',num=2)
print("Results={}".format(res))
```

Optional:

-use crawl=False to load from already crawled dataset,and save crawling time if you already crawled the same thing once.See [url_maps.csv](src/url_maps.csv).  

-num=10 by default, change it to modify the number of recommendations.
