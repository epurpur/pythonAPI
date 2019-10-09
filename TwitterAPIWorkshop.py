#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:09:10 2019

@author: ep9k
"""

from twython import Twython
import tweepy
from datetime import date





############################### Twython
#First you need to install Twython. In the terminal(Mac) or Shell(Windows)... pip install twython

#To find your twitter API keys, go here (after login): https://developer.twitter.com/en/apps/

twython_key = 'iJGWsGU50hpgpHPufeqe7IoAq'                         #Copy and paste your API consumer key here. This is NOT secure and is only being used as an example
twython_secret = 'wj0YmifZhPH5TaY5iGCTDpQGp4rivmFq5DYkPOoegkOLAXsigD'                    #Copy and paste your API consumer secret here. This is NOT secure and is only being used as an example
#
#
python_tweets = Twython(twython_key, twython_secret)                      #This packages your API keys together in a format that Twitter likes
#
#
#Create your query
query = {'q': 'Trump',
         'result_type': 'popular',
         'count': 5,
         'lang': 'en'
         }

#print(type(python_tweets))
results_dict = python_tweets.search(**query)            #creates a DICTIONARY with results. Data is structured in JSON format. **query is a keyword argument          

print(results_dict)

for keys, values in results_dict.items():               
    print(keys)                                         #only two keys (statuses, search metadata)
    
    
print(results_dict['statuses'])                         #looks for values in the 'statuses' key of results_dict. Dictionaries are unordered data types and you find the values by calling the name of each key


first_result = results_dict['statuses'][0]             #within ['statuses'] is a list (of dictionaries). Lists are ordered data types and you can use indexing to parse through the list elements
print(first_result)


for keys, values in first_result.items():              #first_result is now a dictionary. To see all the keys it has, do this again
    print(keys)


print(first_result['text'])                             #prints actual text of the tweet (with URL to original tweet!)


print(first_result['user'])                             #gives a bunch of information about the user who tweeted (I assume) in another DICTIONARY
print(first_result['user']['name'])                     #again, access the values of the keys in this dictionary 


##A batch operation:
statuses = results_dict['statuses']                     
for status in statuses:
    print(status['text'])
    print()
    print()
    





############################### Tweepy
#First you need to install Twython. In the terminal(Mac) or Shell(Windows)... pip install tweepy

tweepy_key = 'your consumer key as string here'                          #Copy and paste your API consumer key here. This is NOT secure and is only being used as an example
tweepy_secret = 'your consumer secret as string here'                    #Copy and paste your API consumer secret here. This is NOT secure and is only being used as an example
tweepy_access_token = 'your access token as string here'                 #Copy and paste your API access token. This is NOT secure and is only being used as an example
tweepy_access_secret = 'your access token secret as string here'         #Copy and paste your API access token secret here. This is NOT secure and is only being used as an example


auth = tweepy.OAuthHandler(tweepy_key, tweepy_secret)
auth.set_access_token(tweepy_access_token, tweepy_access_secret)

api = tweepy.API(auth)

#This example will download your home timeline tweets and print the text to the console
public_tweets = api.home_timeline()                                     #public_tweets is a Status object                        
for tweet in public_tweets:
    print(tweet.text)
    print()

#Work with your own Twitter metadata
user = api.get_user("PurpurErich")
print(user.name)
print()
#
print("My Followers")
for follower in user.followers():
    print(follower.name)
    


#I've use the datetime module to make a simple tweet on my twitter account.
api.update_status(f"Hello from Tweepy on {date.today()}")                                 #makes a status update to your twitter page. You can make a twitter bot using either Tweepy or Twython

#You can build much more sophisticated twitter bots. You can watch for Twitter activity for various hashtags, follow people, automatic retweets, etc
#To see code examples, go here: https://realpython.com/twitter-bot-python-tweepy/




        
        
        






