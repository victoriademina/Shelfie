from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos


# https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        title = request.form['title']
        status = request.form['status']
        todos.insert_one({'title': title, 'status': status})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))
