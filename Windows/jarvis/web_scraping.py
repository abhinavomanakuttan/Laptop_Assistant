'''How are Datasets Created by Scraping the Web?
There are so many libraries, frameworks, and tools that are used for the task of web scraping. Some of the most common libraries and modules in Python used for web scraping are:

Scrapy
Selenium
BeautifulSoup
Urlib.request
All of the above Python libraries and modules are great for scraping data from websites. After scraping the data, the data is prepared so that it can be stored in a CSV file to create a dataset.

Web Scraping to Create a Dataset using Python
Now let’s see how to create a dataset by scraping the web using Python. For this task, I will be using the BeautifulSoup library in Python. Here I am going to search for a random term on Google and then I will collect the data from the very first page that Google shows me.


So, I searched for “comparison of programming languages” on Google and got this article as the first result. Let’s see how we can scrape data from this web page to create a dataset. Below is how we can use the BeautifulSoup library in Python for the task of web scraping to create a dataset:
'''
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

with open("language.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)
   
  
import pandas as pd
a = pd.read_csv("language.csv")
a.head()
