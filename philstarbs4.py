from operator import truediv
from bs4 import BeautifulSoup
import requests

philstar = ('https://www.philstar.com/')

urls = []
section_names = []

data = requests.get(philstar)
soup = BeautifulSoup(data.text, 'html.parser')

main_link = soup.find('ul', {'id': 'main-navig'}).find_all('a')

for a in main_link:
    sct = a.text
    section_names.append(sct.strip())

for hrefs in main_link:
    urls.append(hrefs.attrs['href'])

urls.pop(0)
section_names.pop(0)
article_info = {}

for x in range(len(section_names)):
    article_info[section_names[x]] = urls[x]

#print(article_info)
#print(urls)
"""
{'HEADLINES': 'https://www.philstar.com/headlines', 
'OPINION': 'https://www.philstar.com/opinion', 
'NATION': 'https://www.philstar.com/nation', 
'WORLD': 'https://www.philstar.com/world', 
'BUSINESS': 'https://www.philstar.com/business', 
'SPORTS': 'https://www.philstar.com/sports', 
'ENTERTAINMENT': 'https://www.philstar.com/entertainment', 
'LIFESTYLE': 'https://www.philstar.com/lifestyle', 
'OTHER SECTIONS': 'https://www.philstar.com/other-sections'}
"""

def section_links(url):
    article_link = []
    link = requests.get(url)
    soup = BeautifulSoup(link.text, 'html.parser')

    for links in soup.find('div', {'class': 'carousel__items'}).find_all('a'):
        attr = links.attrs['href']
        if attr.startswith("https://www.philstar.com/"):
            article_link.append(attr)

    for links in soup.find('div', {'id': 'news_main'}).find_all('a'):
        attr = links.attrs['href']
        if attr.startswith("https://www.philstar.com/"):
            article_link.append(attr)
    
    return list(set(article_link))

sections = list(article_info.values())
#print(sections)
#print(section_links(sections[0]))

