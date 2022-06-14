# Part 2/3: MongaDB and Flask

# Automates browser actions
from splinter import Browser
import requests

# Parses the HTML
from bs4 import BeautifulSoup
import pandas as pd
import time

# Used for scrape with Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Execute all of the scraping code from 'missions_to_mars.ipynb' and return one Python dictionary containing all scraped data
def scrape():

    # Initialize browser using webdriver (Chrome)
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # 1. Mars News Scraping
    
    # Set link/url to a variable to visit Mars News Site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Let browser sleep for 1 second
    time.sleep(1)

    # Set up HTML parser (converting browser html to a soup object and quit the browser)
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Get title using select_one (first tag that matches selector) from soup object and selector ('div.list_text')
    site_elem = news_soup.select_one('div.list_text')
    site_elem.find("div", class_='content_title')

    # Create variable ('news_title') to save first tag using the parent element ("div", class_='content_title')
    news_title = site_elem.find("div", class_='content_title').get_text()
 

    # Create variable ('news_p') to save paragraph text using the parent element ("div", class_='article_teaser_body')
    news_p = site_elem.find('div', class_='article_teaser_body').get_text()

    # 2. JPL Mars Space Images - Featured Images

    # Set link/url to a variable to visit Mars News Site
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Select 'FULL IMAGE' button to select the latest featured image
    full_image_btn = browser.find_by_tag('button')[1]
    full_image_btn.click()

    # Set up HTML parser (converting browser html to a soup object and quit the browser)
    html = browser.html
    mars_img_soup = soup(html, 'html.parser')

    # Find relative image url ('image/featured/mars3.jpg')
    mars_img_rel_url = mars_img_soup.find('img', class_='fancybox-image').get('src')

    # Create absolute (complete) url with base url
    featured_image_url = f'https://spaceimages-mars.com/{mars_img_rel_url}'

    # 3. Mars Facts

    # Have Pandas read second table [1] and place into a dataframe
    mars_facts_df = pd.read_html('https://galaxyfacts-mars.com')[1] # Facts about Mars only

    # Define column names and set_index
    mars_facts_df.columns=['Description', 'Value']
    mars_facts_df.set_index('Description', inplace=True)    

    # Convert dataframe to HTML table
    mars_facts_tr_html = mars_facts_df.to_html()

    # Strip unwanted newlines to clean up the table
    mars_facts_tr_html = mars_facts_tr_html.replace('\n', '')

    # Strip table tag for easier html formatting
    mars_facts_tr_html = mars_facts_tr_html.replace("<table border=\"1\" class=\"dataframe\">", "").\
                                                                    replace("</table>","").strip()

    # 4. Mars Hemispheres

    # Set link/url to a variable to visit Astrogeology Site
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Create list variable to hold images and titles 
    hemisphere_image_urls = []

    # For loop to retrieve the image urls and titles of each hemisphere
    for hemi in range(4): # 4 is the number of image urls/titles we have to loop through
        browser.links.find_by_partial_text('Hemisphere')[hemi].click()  # Splinter used to find partial text in links 
    
        # HTML parser and create soup variable
        html = browser.html
        hemisphere_soup = soup(html, 'html.parser')
    
        # Web scraping using specific selector to locate the titles and image urls
        title = hemisphere_soup.find('h2', class_='title').text
        img_url = hemisphere_soup.find('li').a.get('href')
    
        # Store web scraping findings into a dictionary and append to list
        hemispheres = {}
        hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
        hemispheres['title'] = title
        hemisphere_image_urls.append(hemispheres)
    
    # Repeat steps to browse all links
    browser.back()
    
    # Quit browser
    browser.quit()

    # Store scaped values in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts_tr_html": mars_facts_tr_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Returns results
    return mars_data

 

  
