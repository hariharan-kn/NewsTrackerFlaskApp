from time import sleep
from unicodedata import category
from apscheduler.schedulers.background import BackgroundScheduler
import threading
from newsapi import NewsApiClient
import sys
from flask import Flask
import collections

#Creating a parallel news api listener
def prompt():
    global articles
    all_articles = newsapi.get_top_headlines(category='business',language='en',page=2)
    if collections.Counter(all_articles)!=collections.Counter(articles):
        print("New News")
        articles = all_articles
        #Sending Email using sendgrid
    else:
        print("Old News ")
def backgroundScheduler():
    sched = BackgroundScheduler()
    sched.add_job(prompt,'interval', seconds=10)
    sched.start()
    while True:
        pass


#Running a Flask Server

app = Flask("__main__")

@app.route("/")
def home():
    return "Hi"

articles = []
newsapi = NewsApiClient(api_key='16f8562d339c462ba4c5863e27f39bca')
t = threading.Thread(target=backgroundScheduler)
t.start()
app.run()

