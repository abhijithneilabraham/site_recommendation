# site_recommendation
A recommender system to crawl multiple sites and get recommendation for sites to visit.

`git clone https://github.com/abhijithneilabraham/site_recommendation`.  


`cd src`

```pip install -r requirements.txt```

Example.  
```
from recommender import Recommender
r=Recommender(['http://abhijithneilabraham.me/eywabot/','http://abhijithneilabraham.me/','https://abhisharmab.github.io/','https://karuvally.github.io/'],crawl=True)
res=r.recommend('http://abhijithneilabraham.me/eywabot/models/Classifer/',num=2)
print("Results={}".format(res))
```



