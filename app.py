from crypt import methods
import threading
from newsapi import NewsApiClient
from flask import Flask,render_template,request
#from hourlyScheduler import schedule

#Running a Flask Server
app = Flask("__main__")

@app.route("/",methods=['POST','GET'])
def home():
    if request.method=='POST':
        print(request.form['username'],request.form['username'])
    return render_template("login.html")




app.run()

