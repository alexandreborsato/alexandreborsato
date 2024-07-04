#Here is the Python code to implement the web scraper that extracts data from multiple pages and stores results in a SQLite database:

import requests
import sqlite3
#import bs4
from bs4 import BeautifulSoup

# Connect to SQLite database
conn = sqlite3.connect('scraped_data.db')
c = conn.cursor() 

# Create table to store scraped data  
c.execute('''CREATE TABLE IF NOT EXISTS data 
              (name text, phone text, address text)''')

# List of URLs to scrape
urls = [
    'https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html',
    'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console',
    'https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html'
]

# Loop through URLs and scrape data
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Extract data from page
    name = soup.find(id="name").get_text()  
    phone = soup.find(id="phone").get_text()
    address = soup.find(id="address").get_text()
    
    # Insert data into database
    c.execute("INSERT INTO data VALUES (?, ?, ?)", (name, phone, address))

conn.commit()
conn.close()
