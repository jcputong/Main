from ntpath import join
from bs4 import BeautifulSoup
import requests
import re

url = ("https://www.philstar.com/world/2022/09/10/2208767/charles-iii-proclaimed-new-king-historic-ceremony")
url1 = ('https://www.philstar.com/opinion/2022/08/12/2202136/high-maintenance')
url2 = ("https://www.philstar.com/nation/2022/09/08/2208181/mandaluyong-hit-and-run-suspect-pleads-not-guilty")
data = requests.get(url)

#print(data.text)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.title.text #High maintenance | Philstar.com
title = title.split('|')[0].strip()
#print(title)

section = soup.find('div', class_='article__section-name').text
"""
section = soup.find('div', {'class': 'article__section-name'}).text 
>> this will also yield same result
"""
#print(section)

body = soup.find('div', {'class': 'article__writeup'}).find_all('p')
body_list = []

for p in body:
    body_list.append(p.text.strip())
    
body = ''.join(body_list)
body = re.sub('\*', '', body).strip()
body = re.sub(' +', ' ', body)
#print(body)

date = soup.find('div', class_='article__date-published').text
date = date.split('|')[0].strip()
#print(date)

author = soup.find('div', {'class': 'article__credits-author-pub'}).text
if author.__contains__('Philippine Star'):
    author = author.split('-')[0]
else:
    pass

article = {
    'Title': title,
    'Section': section,
    'Author': author,
    'Date': date,
    'Context': body
}

print(article)