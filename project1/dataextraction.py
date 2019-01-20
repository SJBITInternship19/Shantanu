import os
try:
	os.system("pip install -r reqirements.txt")
	os.system("cls")
except: pass
import tweepy
import csv


access_token = "2365687802-KDauSAchfjCNxAEhEw0YkAAh90m3V2YPk2rHGKB"
access_secret = "6JRlnyUPI8ks0OyA6WCTYA2UhHO4qpb9AmCoEr6RE3Hmt"
consumer_key = "HK1N9jXOVyrObI8CleHSayRjg"
consumer_secret = "ga7XXmbKjayaoZ5AdOpR42bBPoCVkhJLY1dPJAYvLlmxhcpM3M"

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)
csvfile=open('uri.csv','a')
csvwriter = csv.writer(csvfile)
try: 
	for tweet in tweepy.Cursor(api.search,q="uri",count=100,lang="en",since="2017-04-03").items():
		print(tweet.created_at, tweet.text)
		csvwriter.writerow([tweet.text.encode('utf-8')])
except: pass
os.system("pip freeze > requirements.txt")