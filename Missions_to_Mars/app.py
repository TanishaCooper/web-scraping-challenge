# Part 3: Flask


from cgitb import html
import code
from re import template
import scrape_mars
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo

# Create Flask app instance and use flask_pymongo to setup MongoDB connection
app=Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"  # Open MongoDB app to find MONGO_URL config [Flask-PyMongo - https://flask-pymongo.readthedocs.io/en/latest/]
mongo = PyMongo(app)

# Define your routes that renders index.html template and finds documents from MongoDB
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

if __name__== "__main__":
    app.run(debug=True)



