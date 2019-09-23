#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:09:10 2019

@author: ep9k
"""

from twython import Twython
import json
import pandas as pd

#consumer_key = 'your consumer key as string here'         #Copy and paste your API consumer key here. This is NOT secure and is only being used as an example
#consumer_secret = 'your consumer secret as string here'   #Copy and paste your API consumer secret here. This is NOT secure and is only being used as an example
consumer_key = 'iJGWsGU50hpgpHPufeqe7IoAq'
consumer_secret = 'wj0YmifZhPH5TaY5iGCTDpQGp4rivmFq5DYkPOoegkOLAXsigD'


python_tweets = Twython('iJGWsGU50hpgpHPufeqe7IoAq', 'wj0YmifZhPH5TaY5iGCTDpQGp4rivmFq5DYkPOoegkOLAXsigD')
#python_tweets = Twython(f"{consumer_key}, {consumer_secret}")


#Create your query
query = {'q': 'University of Virginia',
         'result_type': 'popular',
         'count': 5,
         'lang': 'en'
         }

results_dict = python_tweets.search(**query)            #creates a DICTIONARY with results
#for keys, values in results_dict.items():               
#    print(keys)                                         #only two keys (statuses, search metadata)
    
    
#print(results_dict['statuses'])                         #looks for values in the 'statuses' key of results_dict. Dictionaries are unordered data types and you find the values by calling the name of each key

#first_result = results_dict['statuses'][0]             #within ['statuses'] is a list (of dictionaries). Lists are ordered data types and you can use indexing to parse through the list elements
#print(first_result)



#for keys, values in first_result.items():              #first_result is now a dictionary. To see all the keys it has, do this again
#    print(keys)

#print(first_result['text'])                             #prints actual text of the tweet (with URL to original tweet!)


#print(first_result['user'])                             #gives a bunch of information about the user who tweeted (I assume) in another DICTIONARY
#print(first_result['user']['name'])                     #again, access the values of the keys in this dictionary 

#Some batch operations:
statuses = results_dict['statuses']                     
for item in statuses:
    print(item['text'])
    print()
    
#strip the url out of each tweet
list_of_urls = []







