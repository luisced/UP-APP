# scrapping library for python
import requests
import os
import sys
# library for parsing html
from bs4 import BeautifulSoup as bs

# url of the website
url = "https://10fastfingers.com/typing-test/spanish"

# get the html of the website
r = requests.get(url)

# parse the html
soup = bs(r.content, 'html.parser')

# beautify the html
print(soup.prettify())
