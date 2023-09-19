```
Last updated 08/24/23
```

## **About Me**

Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu
    Brown Science & Engineering Library room I046


I'm a part of a group called [research data services](https://data.library.virginia.edu/) and I do these things:
    
    1. Serve as Liaison to various departments in the sciences & engineering
    2. Teach workshops and classes (like this one)
    3. Help people with research projects
    4. Random other things as they come up

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)

## Other Upcoming Workshops

| Workshop | Date | Time |
| ---- | ---- | ---- |
| Intro to Python pt 1                                                |       Tuesday 8/29   |  12:00 - 1:30pm
| Intro to Python pt 2                                                |       Tuesday 9/5    |  12:00 - 1:30pm
| Intro to Version Control w/ Git + Github                            |       Wednesday 9/6  |  1:00 - 2:30pm
| Python Data Analysis + Visualization                                |       Tuesday 9/12  |  12:00 - 1:30pm
| Intro to Regular Expressions                                        |       Wednesday 9/13 |  1:00 - 2:30pm
| Python and APIs                                                     |       Tuesday 9/19   |  12:00 - 1:30pm
| Geospatial Data + Mapping in Python                                 |       Tuesday 9/26   |  12:00 - 1:30pm
| Python Web Dashboards w/ Streamlit                                  |       Tuesday 10/10  |  12:00 - 1:30pm
 

This is an introduction workshop to APIs. Specifically, we will be using python to communicate with the API for various applications, but first we should start with the basics

## **What is an API?**
*The following excerpt is taken from [this site](https://www.mulesoft.com/resources/api/what-is-an-api)*
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. By establishing a common set of rules for exchanging information, APIs make it easier for two parties to communicate with eachother. Each time you use an app like Instagram, find a song you like on Spotify, or check the weather on your phone, you’re using an API.

For example, when you use an application on your device, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions and then returns data to you. This data might be in the form of JSON or it might just be a response code <200>. This is what an API is - all of this happens via API.

The API states the rules in order for this communication to happen. 

An analog example in real life...
If you go to a restaurant, you sit down at a table and look at a menu. The server comes and takes your order. Your order is then taken to the kitchen where they prepare the food. In this case, the server is the API, which is a layer of interaction between the client and the kitchen. You (probably) can't go directly into the kitchen and order food. The waiter is the intermediary that takes your information and interprets it into a form the kitchen can understand. The information (the food in this case) is then sent back to you, the client. 


Good example of an HTTP URL: https://newsapi.org/


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

## **Requests**
Requests is a Python module used to make HTTP requests. Basically, you structure an HTTP request and send it to an endpoint

## **Conda**
Conda is a special program used to install python packages to your system. Pip is another common one. Basically, base 
installation of python provides many built in functions and libraries (some of which must be imported). But out there in the 
world exist many, many other libraries which are available for you to use. These are basically like add-ons on top of 
python. Conda is the built-in package library installed with the Anaconda distribution. 

## **Jupyter Lab**
Jupyter Notebooks are web applications that allow you a nice way to present and share live code and accompanying equations, 
visualizations, etc. To me, they read and look like an interactive blog post. The author walks through the code step by step, 
adding explanation and comments. The user can run and edit the code live. The next generation of Jupyter Notebooks is Jupyter 
Lab and to be honest I can't tell the difference between them so I continue to use Jupyter Notebooks. Visit the [Project 
Jupyter Homepage](https://jupyter.org/) to learn more.

Jupyter Notebooks are web-based applications and are client/server applications. When you launch a Jupyter notebook, you might 
notice that a web-server launches as well. We will be running this locally today, but you can also host a Jupyter notebook on 
a remote server. You access the client through the web browser.

## **Open Weather Map**

*Get the API documentation here: https://openweathermap.org/api

*Read the 'How to get started' page: https://openweathermap.org/appid

*Current Weather API docs: https://openweathermap.org/current

*5 Day Forecast API docs: https://openweathermap.org/forecast5

Open Weather Map provides an API which, upon request, returns weather data in JSON format. Open Weather map also provides
various subcription levels that provide access to different data, though some data is available for free. 


## **Self Help - You don't need to remember all of this!**

Honestly, you don't need to remember most of it. Here are the resources I use when looking for answers:

ChatGPT
* ChatGPT has quickly made huge changes to the programming landscape. It is a hugely powerful tool **If you use it the right way!**. I think it is a somewhat slippery slope of how to advise new programmers to use ChatGPT (or other AI tools) so I will refer to some best practices. My personal opinion is that you should use AI minimally when you are starting. When you have a better grasp of basic fundamentals, then you can include AI and greatly increase your speed. **Never accept ChatGPT code verbatim!** Always double check it before including it in your workflows.
* [How to Effectively Learn to Program w/ ChatGPT](https://towardsdatascience.com/how-to-effectively-start-coding-in-the-era-of-chatgpt-cfc5151e1c42)
* [Corey Schafer's "How to use ChatGPT"](https://www.youtube.com/watch?v=jRAAaDll34Q)





