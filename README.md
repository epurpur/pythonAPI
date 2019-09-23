This is an introduction workshop to APIs. Specifically, we will be using the python API for various applications, but first we should start with the basics

## **What is an API?**
*The following excerpt is taken from [this site](https://www.mulesoft.com/resources/api/what-is-an-api)*
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

When you use an application on your mobile phone, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. This is what an API is - all of this happens via API.

Imagine you’re sitting at a table in a restaurant with a menu of choices to order from. The kitchen is the part of the “system” that will prepare your order. What is missing is the critical link to communicate your order to the kitchen and deliver your food back to your table. That’s where the waiter or API comes in. The waiter is the messenger – or API – that takes your request or order and tells the kitchen – the system – what to do. Then the waiter delivers the response back to you; in this case, it is the food.

Here is a real-life API example. You may be familiar with the process of searching flights online. Just like the restaurant, you have a variety of options to choose from, including different cities, departure and return dates, and more. Let us imagine that you’re booking you are flight on an airline website. You choose a departure city and date, a return city and date, cabin class, as well as other variables. In order to book your flight, you interact with the airline’s website to access their database and see if any seats are available on those dates and what the costs might be.

However, what if you are not using the airline’s website––a channel that has direct access to the information? What if you are using an online travel service, such as Kayak or Expedia, which aggregates information from a number of airline databases?

The travel service, in this case, interacts with the airline’s API. The API is the interface that, like your helpful waiter, can be asked by that online travel service to get information from the airline’s database to book seats, baggage options, etc. The API then takes the airline’s response to your request and delivers it right back to the online travel service, which then shows you the most updated, relevant information.

## **RESTful APIs**##
REST determines how the API looks like. It stands for “Representational State Transfer”. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.

Each URL is called a request while the data sent back to you is called a response. Basically, you submit a URL to the API, and the API delivers data back to you conforming to the parameters you asked for. Twitter's API is an example of a REST API. 

## **Twitter API**##
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

## **Get Credentials (API Key)**##

*Unfortunately, there is a delay between your request for a new twitter API key and when they deliver it to you. Please do this before class if possible!*

Before using the Twitter API, you first need a Twitter account, and to have obtained some credentials. The process of getting credentials could change with time, but currently it is as follows:

Visit the Application Management page at https://apps.twitter.com/, and sign in with your Twitter account
* Click on the "Create New App" button, fill in the details and agree the Terms of Service
* Navigate to "Keys and Access Tokens" section and take a note of your Consumer Key and Secret
* In the same section click on "Create my access token" button
* Take note of your Access Token and Access Token Secret
And that's all. The consumer key/secret is used to authenticate the app that is using the Twitter API, while the access token/secret authenticates the user. All of these parameters should be treated as passwords, and should not be included in your code in plain text.
