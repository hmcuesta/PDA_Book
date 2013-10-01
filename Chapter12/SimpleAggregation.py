from pymongo import MongoClient

con = MongoClient()
db = con.Corpus
tweets = db.tweets


results = tweets.aggregate([
         {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
     ])


for doc in results["result"]:
    print(doc)
