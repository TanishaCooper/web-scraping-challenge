# Part 3: Flask

import code
from distutils.log import debug
from readline import append_history_file
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask app instance and use flask_pymongo to setup MongoDB connection
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017"  # Open MongoDB app to find MONGO_URL config [Flask-PyMongo - https://flask-pymongo.readthedocs.io/en/latest/]
mongo = PyMongo(app)

# Define your routes that renders index.html template and finds documents from MongoDB
@app.route("/")
def index():

    # Locate/Find mars_data
    try:
        mars = list(mongo.db.collection.find())[-1]
    except:
        mars = {}

    # Pass mars data to return template and data
    return render_template("index.html", mars=mars)

# Define route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    mars = scrape_mars.scrape()

    # Store results into a dictionary
    mars_dict = {
        "news_title": mars["news_title"],
        "news_p": mars["news_p"],
        "featured_image_url": mars["featured_image_url"],
        "mars_facts_tr_html": mars["mars_facts_tr_html"],
        "hemisphere_image_urls": mars["hemisphere_image_urls"]
    }

    # Insert mars_dict into MongoDB database
    mongo.db.collection.insert_one(mars_dict)

    # Redirect  back to homepage
    return redirect(url_for("index"), code=302)

if __name__== "__main__":
    app.run(debug=True)



