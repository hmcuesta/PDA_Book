from twython import Twython

ConsumerKey  = "..."
ConsumerSecret = "..."
AccessToken = "..."
AccessTokenSecret = "..."


twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)
				  
				  
result = twitter.search(q="python")

for status in result["statuses"]:
    print("user: {0} text: {1}".format(status["user"]["name"], status["text"]))
 

