from tinydb import TinyDB, Query
from flask import Flask, render_template, request
from helper import Meals
app = Flask(__name__)
db = TinyDB('store/db.json')
User = Query()
#   db.insert({'name': 'John', 'age': 30})


@app.route("/")
def hello_world():
    return f"<h1>200</h1>"

@app.route("/create", methods=['POST', 'GET'])
def create_meal():
    if request.method == 'POST' and int((request.args.get('date'))) > 0:
        date = request.args.get('date')
        main = request.args.get('main')
        side1 = request.args.get('side1')
        side2 = request.args.get('side2')
        newMeal = Meals(date, main, side1, side2)
        print(newMeal.date)
        db.insert({'date': newMeal.date, 'main': newMeal.main, 'sides': [newMeal.side1, newMeal.side2]})
        return f"<p>201</p>"
    else:
        return("<h1>Err 404</h1>")

@app.route("/meals")
def loadMeal():
    if request.method == 'GET':
        date = request.args.get('date')
        results = db.search(User.date == date)
        #results = db.all()
        return f"<h1>{results}</h1>"
    else:
        return("<h1>Err 404</h1>")
