from bson.code import Code
from pymongo import MongoClient

con = MongoClient()
db = con.Corpus
tweets = db.tweets

map = Code("function(){ emit(this.via, 1); }")

reduce = Code("""function(key, values) { 
	     	    var res = 0;
	            values.forEach(function(v){ res += 1})
	            return {count: res}; 
              }""")

result = tweets.map_reduce(map,reduce,"filtering", limit = 100)

print(result)

for doc in db.filtering.find():
    print(doc)
