from flask import Flask, render_template, request, redirect, url_for, session, flash, logging
import datetime
import os
import random

app = Flask(__name__)

from models import google, yahoo, duck, ecosia

# http://localhost:5000/
@app.route('/',)
def index():
    return render_template('home.html')


# http://localhost:5000/services
@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == "POST":
        result = request.form
        search = result['search']
        google_link, google_text= google(search)
        google_data = zip(google_link,google_text)
        yahoo_link,yahoo_text = yahoo(search)
        yahoo_data = zip(yahoo_link,yahoo_text)
        duck_link,duck_text = duck(search)
        duck_data = zip(duck_link,duck_text)
        ecosia_link,ecosia_text = ecosia(search)
        ecosia_data = zip(ecosia_link,ecosia_text)
        if result == '':
            return render_template('home.html')
        else:
            return render_template('results.html', google=google_data, yahoo=yahoo_data, duck=duck_data, ecosia=ecosia_data)



if __name__ == "__main__":
    app.run()
