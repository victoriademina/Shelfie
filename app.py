from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
books = db.books


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        title = request.form['title']
        status = request.form['status']
        books.insert_one({'title': title, 'status': status})
        return redirect(url_for('index'))
    all_books = books.find()
    return render_template('index.html', books=all_books)


@app.post('/<id>/delete/')
def delete(id):
    books.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))
