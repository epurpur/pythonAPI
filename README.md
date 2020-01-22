## **About Me**

Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu
    Brown Science & Engineering Library room I046


I'm a part of a group called [research data services](https://data.library.virginia.edu/) and I do these things:
    
    1. Serve as Liaison to various engineering departments
    2. Teach workshops and classes (like this one)
    3. Help people with research projects
    4. Random other things as they come up

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)

~R workshops
  * Data Wrangling in R                                       Tuesday, 1/28  10:00 - 12:00 Brown 133
  * Data Visualization in R                                   Tuesday, 2/4   10:00 - 12:00 Brown 133
  
~Python Workshops
  * Data Visualization with MatPlotLib                        Tuesday, 2/4   2:00 - 4:00 Brown 133
  * Web Scraping in Python                                    Tuesday, 2/11  2:00 - 4:00 Brown 133


We are partnering with Research Computing to offer all workshops in one series this semester!
[Research Computing](https://www.rc.virginia.edu/)



This is an introduction workshop to APIs. Specifically, we will be using python to communicate with the API for various applications, but first we should start with the basics

## **What is an API?**
*The following excerpt is taken from [this site](https://www.mulesoft.com/resources/api/what-is-an-api)*
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. By establishing a common set of rules for exchanging information, APIs make it easier for two parties to communicate with eachother. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

When you use an application on your mobile phone, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. This is what an API is - all of this happens via API.

Here is a real-life API example. You may be familiar with the process of searching flights online. You have a variety of options to choose from, including different cities, departure and return dates, and more. Let us imagine that you’re booking you are flight on an airline website. You choose a departure city and date, a return city and date, cabin class, as well as other variables. In order to book your flight, you interact with the airline’s website to access their database and see if any seats are available on those dates and what the costs might be.

However, what if you are not using the airline’s website––a channel that has direct access to the information? What if you are using an online travel service, such as Google Flights or Expedia, which aggregates information from a number of airline databases?

The travel service, in this case, interacts with the airline’s data via an API. The API is the interface that can be asked by that online travel service to get information from the airline’s database to book seats, baggage options, etc. The API then takes the airline’s response to your request and delivers it right back to the online travel service, which then shows you the most updated, relevant information.

## **REST APIs**
Stands for “Representational State Transfer” is an architectural style for APIs that relies on the HTTP protocol and JSON data format to send and receive messages. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.

Each URL is called a request while the data sent back to you is called a response. Basically, you submit a URL to the API, and the API delivers data back to you conforming to the parameters you asked for. OpenWeatherMap and Twitter APIs are examples of REST APIs.

For data security, uses HTTPS, which is the underlying transport mechanism. REST is generally the API style of choice today.


## **SOAP APIs**
Stands for "Simple Object Access Protocol" and is an API protocol that uses XML data format in order to exchange information. Uses extra overhead in order to package and un-package the data, for data security.


## **JSON** 
JSON is an acronym for JavaScript Object Notation. Basically it is a easy to use data interchange format. It is easy for 
humans to read and write, and easy for machines to parse and create. JSON is a text format that is language independent. It 
is built on name-value pairs. In python this is referred to as a dictionary. It has different names in other languages.

For our concerns today, we submit a query to the endpoint via a URL and the response is returned as JSON data. Then we parse 
this data just like we would any python dictionary. 




## **Open Weather Map**

*Get the API documentation here: https://openweathermap.org/api
*Read the 'How to get started' page: https://openweathermap.org/appid
*Current Weather API docs: https://openweathermap.org/current
*5 Day Forecast API docs: https://openweathermap.org/forecast5

Open Weather Map provides an API which, upon request, returns weather data in JSON format. Open Weather map also provides
various subcription levels that provide access to different data, though some data is available for free. 


~~~~~~~~~~~~~~~~~~~~~~~~`
## **Get Credentials (API Key)**

*Unfortunately, there is a delay between your request for a new twitter API key and when they deliver it to you. You will also need to create an account with Twitter. Please do this before class if possible!*

Before using the Twitter API, you first need a Twitter account, and to have obtained some credentials. The process of getting credentials could change with time, but currently it is as follows:

Visit the Application Management page at https://apps.twitter.com/, and sign in with your Twitter account
* Click on the "Create New App" button, fill in the details and agree the Terms of Service
* Navigate to "Keys and Access Tokens" section and take a note of your Consumer Key and Secret
* In the same section click on "Create my access token" button
* Take note of your Access Token and Access Token Secret
And that's all. The consumer key/secret is used to authenticate the app that is using the Twitter API, while the access token/secret authenticates the user. All of these parameters should be treated as passwords, and should not be included in your code in plain text.

## **Twitter API**
*The following is taken from [Stack Abuse](https://stackabuse.com/accessing-the-twitter-api-with-python/)*

There are many APIs on the Twitter platform that software developers can engage with, with the ultimate possibility to create fully automated systems which will interact with Twitter. While this feature could benefit companies by drawing insights from Twitter data, it's also suitable for smaller-scale projects, research, and fun. Here are a few of the most notable APIs provided by Twitter:

Tweets: searching, posting, filtering, engagement, streaming etc.
Ads: campaign and audience management, analytics.
Direct messages (still in Beta): sending and receiving, direct replies, welcome messages etc.
Accounts and users (Beta): account management, user interactions.
Media: uploading and accessing photos, videos and animated GIFs.
Trends: trending topics in a given location.
Geo: information about known places or places near a location.
There are many more possibilities with the Twitter APIs, which are not included in this list. Twitter is also constantly expanding its range of services by adding new APIs from time to time, and updating existing ones.

## **Python Wrappers for Twitter**

Perhaps "wrapper" is a better term for how to describe Twitter's python API, because the following examples are using python specific libraries to create code to "wrap" around the API to do various things. I will give examples with a couple libraries I have used, though there are many more. Don't hesitate to use another one you already know or like better than these!

**Twython**

*Get the docs here: https://twython.readthedocs.io/en/latest/
*"Twython is an actively maintained, pure python wrapper for the Twitter API..."

To experiment on your own, take a look at the documentation. Particularly the "starting out" link: https://twython.readthedocs.io/en/latest/usage/starting_out.html

**Tweepy**

*Get the docs here: https://tweepy.readthedocs.io/en/latest/
*"Tweepy is an easy to use Python library for accessing the Twitter API"

Great article on the background of Tweepy, the Twitter API, and how to create a Twitter bot here: https://realpython.com/twitter-bot-python-tweepy/



