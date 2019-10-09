#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:37:20 2019

@author: ep9k
"""

import requests
import json
    

############################### Open Weather Map
#Open Weather map is a weather forecast site with a great, easy to use, API.
#API documentation: https://openweathermap.org/api

#First you need to install requests. In the terminal(Mac) or Shell(Windows)... pip install requests


app_id = 'copy and paste your app id here'                                              #Note: this is NOT secure and is only being used for example purposes

#Each city in the world has a unique id number. There are over 1,000,000 so I have given you a few to start with.
city_id_dict = {'Charlottesville': 4752046,                                         #Charlottesville's forecast seems to be wrong??
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
                'Sao Paulo': 3448439,
                'Bogota': 3688689,
                'Havana': 3553478}

city_name = 'Oslo'                                               #change the city name here
city_id_string = str(city_id_dict[f'{city_name}'])                                         

#Make a request to get today's weather
request = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID={app_id}&id={city_id_string}&units=imperial')               #this actually makes the request to the API via the URL with correct parameters

json_data = json.loads(request.text)                                                #json_data is now a dictionary object
print(json_data)

#for keys, values in json_data.items():
#    print(keys)                                                                     #all the interesting data is contained in the 'list' key

print(json_data['list'][0])                                                          #Now we have a list object

#Make a request to get the 5 day forecast
#This gives the forecast at 3 hour intervals for 5 days
request = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id={city_id_string}&APPID=333de4e909a5ffe9bfa46f0f89cad105&units=imperial&')
json_data = json.loads(request.text)


print(json_data)                                                                    #note how messy and hard to read this is. Yet, it is a dictionary


for measurement in json_data['list']:
    print(measurement)
    
    
for daily_measurement in json_data['list']:
    if daily_measurement['dt_txt'][11:20] == '12:00:00':
        print(daily_measurement)
        print(daily_measurement['dt_txt'][:10])
        print(daily_measurement['main']['temp'])                                   #it gets tricky to parse through nested dictionaries
        print()

    
#A cleaner version of the above block
for daily_measurement in json_data['list']:
    time_stamp = daily_measurement['dt_txt'][11:20]
    if time_stamp == '12:00:00':
        day = daily_measurement['dt_txt'][:10]
        temperature = daily_measurement['main']['temp']
        print(f'The temperature in {city_name} on {day} will be {temperature} degrees')
  