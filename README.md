# site_recommendation
A recommender system to crawl multiple sites and get recommendation for sites to visit.

`git clone https://github.com/abhijithneilabraham/site_recommendation`.  


`cd src`

```pip install -r requirements.txt```

Example.  
```
from recommender import Recommender
urls=['http://abhijithneilabraham.me/eywabot/','http://abhijithneilabraham.me/','https://abhisharmab.github.io/','https://karuvally.github.io/']
r=Recommender(urls,crawl=True) #use crawl=False to load from already crawled dataset, see [url maps csv](src/url_maps.csv)
res=r.recommend('http://abhijithneilabraham.me/eywabot/models/Classifer/',num=2)
print("Results={}".format(res))
```





