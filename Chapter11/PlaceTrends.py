from twython import Twython

ConsumerKey  = "..."
ConsumerSecret = "..."
AccessToken = "..."
AccessTokenSecret = "..."
 
 
twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)
				  

				  
result = twitter.get_place_trends(id = 23424977)

if result:
    for trend in result[0].get("trends", []):
        print("{0} \n".format(trend["name"]))
        


