from urllib import request
from bs4 import BeautifulSoup 
import requests
import re

url = "https://www.philstar.com/nation/2022/09/08/2208181/mandaluyong-hit-and-run-suspect-pleads-not-guilty"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

author = soup.find('meta',  {'name':'author'}).find('content')

print(author)