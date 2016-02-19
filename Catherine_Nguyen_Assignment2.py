from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests

#Acquired code from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#Variables that contains the user credentials to access Twitter API 
access_token = "4896621383-NxzYyFiZX4vQA5JPVpR6SdG4hGjGvFFXxlf6HxE"
access_token_secret = "SrxmRsvU9uD8jWxs6H5QNBiM1s1HQ3VxSWGVNgFz7jDQN"
consumer_key = "szr3SlBkCHKorP2FwOVqwm02C"
consumer_secret = "IZbor4la0ROk4a9us6jdzTQXfKVNCa1RFweAd06AJNqaVWYund"

urls = []
urlFile = open('./twitterLinks.txt' , 'w+')

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        if len(urls) >= 1000:
            return False
        #Acquired from Matthew Payne
        json_code = json.loads(data)
        json_code= json_code['user']

        if json.dumps(json_code['url']) != "null":
        #/Matthew Payne
        #Acquired from Gabriel Marquez
            a = json.dumps(json_code['url'])
            a = a[1:-1]
            b = requests.head("http://givemea404.tumblr.com/")
            try:
                b = requests.head(a)
            except requests.exceptions.ConnectionError:
                b.status_code = "derp"
            
            if b.status_code == 200 and  a not in urls:
                urls.append(a)
                urlFile.write(a + '\n')
                print a
        return True
        #/Gabriel Marquez            

    def on_error(self, status):
        pass


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['python', 'javascript', 'ruby'])

    urlFile.close()    
