from bson.code import Code
import csv
from pymongo import MongoClient

con = MongoClient()
db = con.Corpus
tweets = db.tweets

map = Code("""function(){
                this.text.split(' ').forEach(
                    function(word){
                        var txt = word.toLowerCase();
                        if(!(/^@/).test(txt) && txt.length > 3 && !(/^http/).test(txt)){
                            emit(txt,1)
                        }
                    }
                )
            }""")

reduce = Code("""function(key, values) { 
	     	    var res = 0;
	            values.forEach(function(v){ res += 1})
	            return {count: res}; 
              }""")

result = tweets.map_reduce(map,reduce,"TweetWords", query={"sentiment":4})

print(result)

with open("data.csv", "w") as f:

    f_csv = csv.writer(f, delimiter=',')
    f_csv.writerow(["text","size"])

    for doc in db.TweetWords.find().sort("value", direction = -1).limit(50):
        f_csv.writerow([doc["_id"],doc["value"]["count"]+30])   
        print(doc)
