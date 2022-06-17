# **Web-Scraping-Challenge: Mission To Mars**

<center> <img src="https://marshemispheres.com/images/full.jpg" width="600" height="400"> </center>

# <strong>Description</strong>

The challenge was to build a web application that scrapes various websites for data related to the Missions to Mars and display the information in a single HTML page/template.

![Mars App](/Missions_to_Mars/Images/mars_app_1.jpeg)
![Mars App](/Missions_to_Mars/Images/mars_app_2.jpeg)

There are three parts to the Missions to Mars challenge:

1. ***[Scraping](/Missions_to_Mars/mission_to_mars.ipynb)***
2. ***[MongoDB](/Missions_to_Mars/scrape_mars.py)***
3. ***[Flask Application](/Missions_to_Mars/app.py)/[Index Template](/Missions_to_Mars/templates/index.html)***

## Part 1: <strong>Scraping</strong>

### **Mars News**

Using Pandas, BeautifulSoup, Requests/Splinter, and Jupyter Notebook, I scraped Mars News Site to collect the latest news title and corresponding paragraph text. The latest title and corresponding paragraph text was saved in the respective variables, <font color="orange">***'news_title'***</font> and <font color="orange">***'news_p'***</font>. Jupyter notebook used to validate the data scrape properly for transfer to ***[scrape_mars.py](/Missions_to_Mars/scrape_mars.py)***.

![Mars News](/Missions_to_Mars/Images/mars_news_title_p.jpeg)

### **JPL Mars Space Images - Featured Image**

Used Splinter to navigate [Featured Space Image](https://spaceimages-mars.com) site and find the image URL for the current Fetaured Mars Image. Then, I assigned the URL string to a variable called <font color="orange">***'featured_image_url'***</font>

![JPL Mars Space Images](/Missions_to_Mars/Images/jpl_img.jpeg)

### **Mars Facts**

Visited [Mars Facts Webpage](https://galaxyfacts-mars.com) and used ***Pandas*** to scrape the table containing facts about the planet including diameter, mass, etc.

Used ***Pandas*** to convert the <font color="orange">***mars_fact_df***</font> to an HTML table string for later use in the web page.

![Mars Facts](/Missions_to_Mars/Images/mars_facts.jpeg)

### **Mars Hemispheres**

Visted [Astrogeoology Site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars. Ensured that clicked each links to the himspheres in order to find the image URL to the full-resolution image. Saved image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. 

A Python dictionatre was used to store the data using the keys <font color="orange">***'hemisphere_image_urls'***</font> which included each hemisphere's images and titles. Appended the dictionary with the image URL string and the hemisphere title to a list. The list contain one dictionary for each hemisphere.

![Mars Hemispheres](/Missions_to_Mars/Images/hemi_img_title.jpeg)

## Part 2: <strong>MongoDB/Flask</strong>

Used MongoDB with Flask templating to create a new HTML page that displays all the informaiton that was scraped from the URLs above. The latter processed went as such:

1. Converted [missions_to_mars.ipynb](/Missions_to_Mars/mission_to_mars.ipynb) into a Python script called [scraped_mars.py](/Missions_to_Mars/scrape_mars.py) by using the function called <font color="lightblue">***'scraped'***</font> function. 

2. The scrape function executed all the scraping code from the data within the ***scraped_mars.py*** file.

3. The latter returned one Python dictionary (***mars_data***) containing all scraped data.

4. Created a route called ***'/scrape'*** that imported ***'scrape_mars.py'*** script and called the ***'scrape'*** function.

5. Stored the return value in MongoDB as a Python dictionary

6. Created a root route ***'/'*** that queried Mongo database and pass the Mars data into an HTML template for displaying the data.

![Scrape Data Button](/Missions_to_Mars/Images/scrape_data_btn.jpeg)

## Part 3: <strong>Flask Application/Index Template</strong>

Created a template HTML file called [index.html](/Missions_to_Mars/templates/index.html) that will take the Mars data dictionary and display all the data in the appropriate elements. Used the template provided as a guide but used ***bootstrap*** to style the index.html template.
