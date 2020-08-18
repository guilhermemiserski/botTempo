import tweepy
import time
import requests
import json

auth = tweepy.OAuthHandler("xeT4yeI4P1TGXc4NEJhdw46Rb",
                           "n5WCBde7QNNfDbLC21w8NVRSIQ7v6koQRnfkiDAaMZPKjxPxWk")
auth.set_access_token("1219820417482993664-My5rqVu32ny9NZmqYCJcVSi0L63Bp0",
                      "Nr8IcbYhLCIS4YEcA9iFo2ZmdS57MpAcNgyDVWhIV2gxh")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
since_id = 1
new_since_id = since_id
while 1:

    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        try:
                new_since_id = max(tweet.id, new_since_id)
                if tweet.in_reply_to_status_id is not None:
                 continue
                cidade = tweet.text[10:]
                b = '@!?/0123456789'
                for i in range(0,len(b)):
                        cidade = cidade.replace(b[i],"")
                        print(cidade)
                requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=a5f326d36262141e1f7d230ad26db375&lang=pt_br&units=metric')
                tempo = json.loads(requisicao.text)
                tempo = tempo['weather'][0]['description']
                temperatura = json.loads(requisicao.text)
                temperatura = temperatura['main']['temp']
                api.update_status("@" + tweet.user.screen_name + ' condição do tempo: ' + tempo + '\ntemperatura: ' + str(temperatura) + '°C' , in_reply_to_status_id=tweet.id)
                time.sleep(60)
        except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(180)
        except StopIteration:
                break
