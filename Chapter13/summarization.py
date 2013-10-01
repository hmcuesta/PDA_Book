from bson.code import Code
from pymongo import MongoClient

con = MongoClient()
db = con.baseball
games = db.games

map = Code("""function(){
                emit(this.player, this.points);
                
            }""")

reduce = Code("""function(key, values) {
                    var explain = {total:Array.sum(values),
                                   max:Math.max.apply(Math, values),
                                   min:Math.min.apply(Math, values),
                                   avg:Array.sum(values)/values.length}
	     	    return explain;
              }""")

result = games.map_reduce(map,reduce,"_result",query= {"player":"Allen Iverson"})

print(result)

for p in db._result.find():
    print(p)
