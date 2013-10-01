from pymongo import MongoClient

con = MongoClient()
db = con.Corpus
tweets = db.tweets

results = tweets.group(key={"sentiment":1},
                       condition={"via": "kindle2"},
                       initial={"count": 0},
                       reduce="function(obj, prev){prev.count++;}")
for doc in results:
    print(doc)

#>>> 
#{'count': 181.0, 'sentiment': 4.0}
#{'count': 177.0, 'sentiment': 0.0}
#{'count': 139.0, 'sentiment': 2.0}
#>>> 
