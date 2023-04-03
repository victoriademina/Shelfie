from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos


# https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
