import json
from pymongo import MongoClient

con = MongoClient()
db = con.Corpus
tweets = db.tweets

with open("test.txt") as f:
    data = json.loads(f.read())

    for tweet in data["rows"]:
        tweets.insert(tweet)



