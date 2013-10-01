import random as ran
from pymongo import MongoClient

con = MongoClient()
db = con.baseball
games = db.games


players = ["LeBron James",
           "Allen Iverson",
           "Kobe Bryant",
           "Rick Barry",
           "Dominique Wilkins",
           "George Gervin",
           "Dwyane Wade",
           "Jerry West",
           "Pete Maravich",
           "Carmelo Anthony"]


for x in range(100):
    games.insert({ "player" : players[ran.randint(0,9)],
                   "points" : ran.randint(0,100)})

