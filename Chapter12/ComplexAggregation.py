from pymongo import MongoClient

con = MongoClient()
db = con.Corpus
tweets = db.tweets

results = tweets.aggregate([
         {"$group": {"_id": "$via",
                     "avgId": {"$avg": "$id"} ,
                     "maxId": {"$max": "$id"} ,
                     "minId": {"$min": "$id"} ,
                     "count": {"$sum": 1}}}
     ])

for doc in results["result"]:
    print(doc)
