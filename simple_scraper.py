# simple_scraper.py
import requests
from bs4 import BeautifulSoup

def simple_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

url = "http://example.com"
print(simple_scraper(url))
