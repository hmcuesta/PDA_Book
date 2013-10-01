from pymongo import MongoClient

con = MongoClient()
db = con.Corpus
tweets = db.tweets


results = tweets.aggregate([
         {"$group": {"_id": "$via",
                     "count": {"$sum": 1}}},
         {"$sort": {"via":1}},
         {"$limit":10},

          
     ])

for doc in results["result"]:
    print(doc)
