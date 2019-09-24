#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:09:10 2019

@author: ep9k
"""

from twython import Twython
import tweepy
import json
import pandas as pd
from datetime import date
import requests




############################### Twython
#First you need to install Twython. In the terminal(Mac) or Shell(Windows)... pip install twython

#twython_key = 'your consumer key as string here'                          #Copy and paste your API consumer key here. This is NOT secure and is only being used as an example
#twython_secret = 'your consumer secret as string here'                    #Copy and paste your API consumer secret here. This is NOT secure and is only being used as an example
#twython_key = 'iJGWsGU50hpgpHPufeqe7IoAq'
#twython_secret = 'wj0YmifZhPH5TaY5iGCTDpQGp4rivmFq5DYkPOoegkOLAXsigD'
#
#
#python_tweets = Twython(twython_key, twython_secret)                      #This packages your API keys together in a format that Twitter likes
#
#
##Create your query
#query = {'q': 'University of Virginia',
#         'result_type': 'popular',
#         'count': 5,
#         'lang': 'en'
#         }
#
#
#results_dict = python_tweets.search(**query)            #creates a DICTIONARY with results. Data is structured in JSON format          
#
#for keys, values in results_dict.items():               
#    print(keys)                                         #only two keys (statuses, search metadata)
#    
#    
#print(results_dict['statuses'])                         #looks for values in the 'statuses' key of results_dict. Dictionaries are unordered data types and you find the values by calling the name of each key
#
#
#first_result = results_dict['statuses'][0]             #within ['statuses'] is a list (of dictionaries). Lists are ordered data types and you can use indexing to parse through the list elements
#print(first_result)
#
#
#for keys, values in first_result.items():              #first_result is now a dictionary. To see all the keys it has, do this again
#    print(keys)
#
#
#print(first_result['text'])                             #prints actual text of the tweet (with URL to original tweet!)
#
#
#print(first_result['user'])                             #gives a bunch of information about the user who tweeted (I assume) in another DICTIONARY
#print(first_result['user']['name'])                     #again, access the values of the keys in this dictionary 
#
#
##A batch operation:
#statuses = results_dict['statuses']                     
#for status in statuses:
#    print(status['text'])
#    print()
    



############################### Tweepy
#First you need to install Twython. In the terminal(Mac) or Shell(Windows)... pip install tweepy

#tweepy_key = 'your consumer key as string here'                          #Copy and paste your API consumer key here. This is NOT secure and is only being used as an example
#tweepy_secret = 'your consumer secret as string here'                    #Copy and paste your API consumer secret here. This is NOT secure and is only being used as an example
#tweepy_access_token = 'your access token as string here'                 #Copy and paste your API access token. This is NOT secure and is only being used as an example
#tweepy_access_secret = 'your access token secret as string here'         #Copy and paste your API access token secret here. This is NOT secure and is only being used as an example


#tweepy_key = 'iJGWsGU50hpgpHPufeqe7IoAq'
#tweepy_secret = 'wj0YmifZhPH5TaY5iGCTDpQGp4rivmFq5DYkPOoegkOLAXsigD'
#tweepy_access_token = '968923461031747584-7VxWwIwEQdU1jEcxyjB3E5vpc2oFrQL'
#tweepy_access_secret = 'urEMTbfqDLOO5eYXcCvcAtspXy4TV7PT0lDZrYy8Y7rzC'
#
#auth = tweepy.OAuthHandler(tweepy_key, tweepy_secret)
#auth.set_access_token(tweepy_access_token, tweepy_access_secret)
#
#api = tweepy.API(auth)
#
##This example will download your home timeline tweets and print the text to the console
##public_tweets = api.home_timeline()                                     #public_tweets is a Status object                        
##for tweet in public_tweets:
##    print(tweet.text)
##    print()
#
##Work with your own Twitter metadata
#user = api.get_user("PurpurErich")
#print(user.name)
#print()
#
#print("My Followers")
#for follower in user.followers():
#    print(follower.name)
    


#I've use the datetime module to make a simple tweet on my twitter account.
#api.update_status(f"Hello from Tweepy on {date.today()}")                                  #makes a status update to your twitter page. You can make a twitter bot using either Tweepy or Twython

#You can build much more sophisticated twitter bots. You can watch for Twitter activity for various hashtags, follow people, automatic retweets, etc
#To see code examples, go here: https://realpython.com/twitter-bot-python-tweepy/

    

############################### Open Weather Map
#Open Weather map is a weather forecast site with a great, easy to use, API.
#API documentation: https://openweathermap.org/api

#app_id = 'copy and paste your app id here'                                              #Note: this is NOT secure and is only being used for example purposes
app_id = '333de4e909a5ffe9bfa46f0f89cad105'

#Each city in the world has a unique id number. There are over 1,000,000 so I have given you a few to start with.
city_id_dict = {'Charlottesville': 4752031, 
                'New York': 5128581,
                'Chicago': 4887398,
                'Paris': 6455259,
                'Cape Town': 3369157,
                'Beirut': 276781,
                'Dubai': 292223,
                'Shanghai': 1796236,
                'Moscow': 524901,
                'Addis Ababa': 344979,
                'Bangkok': 1609350,
                'Oslo': 6453366,
                'Sao Paolo': 3448439,
                'Bogota': 3688689,
                'Havana': 3553478}

city_id_string = str(city_id_dict['Dubai'])                                         #change the city name here

#Make a request to get today's weather
request = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID={app_id}&id={city_id_string}&units=imperial')               #this actually makes the request to the API via the URL with correct parameters

json_data = json.loads(request.text)                                                #json_data is now a dictionary object
print(json_data)

#for keys, values in json_data.items():
#    print(keys)                                                                     #all the interesting data is contained in the 'list' key

print(json_data['list'][0])                                                          #Now we have a list object

#Make a request to get the 5 day forecast
    
