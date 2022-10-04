# scrapping library for python
import requests
import os
import sys
# library for parsing html
from bs4 import BeautifulSoup as bs

# url of the website
URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
try:
    html = requests.get(URL).text
    document = bs(html, 'html.parser')
    table = document.find('table', class_='infobox vevent')
    python_url = table.find('th', text='Website').next_sibling.a['href']
    version = table.find(
        'th', text='Stable release').next_sibling.strings.__next__()
    logo_url = table.find('img')['src']
    logo = requests.get(f'https:{logo_url}').content
    filename = os.path.basename(logo_url)
    with open(filename, 'wb') as file:
        file.write(logo)
    print(f'{python_url}, {version}, file://{os.path.abspath(filename)}')
except requests.exceptions.ConnectionError:
    print("You've got problems with connection.", file=sys.stderr)
