# Part 3: Flask

import scrape_mars
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo

# Create Flask app instance and use flask_pymongo to setup MongoDB connection
app=Flask(__name__,template_folder='templates')

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"  # Open MongoDB app to find MONGO_URL config [Flask-PyMongo - https://flask-pymongo.readthedocs.io/en/latest/]
# mongo = PyMongo(app)

# Define your routes that renders index.html template and finds documents from MongoDB
@app.route("/")
def home():
    data = mongo.db.data.find_one()
    return render_template("index.html", data=data)

@app.route("/scrape")
def scrape():
    data = mongo.db.data
    mars_data = scrape_mars.scrape()
    data.update({}, mars_data, upsert=True)
    
    return redirect('/', code=302)

if __name__== "__main__":
    app.run(debug=True)



