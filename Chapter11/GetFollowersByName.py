from twython import Twython

ConsumerKey  = "..."
ConsumerSecret = "..."
AccessToken = "..."
AccessTokenSecret = "..."
 

twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)
				  
 
followers = twitter.get_followers_list(screen_name="hmcuesta")

for follower in followers["users"]:
    print(" user: {0} \n name: {1} \n Number of tweets: {2} "
          .format(follower["screen_name"],
                  follower["name"],
                  follower["statuses_count"]))
   
