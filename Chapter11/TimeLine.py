
from twython import Twython

 
ConsumerKey  = "..."
ConsumerSecret = "..."
AccessToken = "..."
AccessTokenSecret = "..."
 
twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)
				  
				  
time = twitter.get_user_timeline(screen_name = "stanfordeng", count = 5)
for tweet in time:
    print(" User: {0} \n Created: {1} \n Text: {2} "
          .format(tweet["user"]["name"],
                  tweet["created_at"],
                  tweet["text"]))



