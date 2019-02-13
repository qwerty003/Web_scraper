import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.prothomalo.com/')
soup = BeautifulSoup(r.text, 'html.parser')
titles = {}
for div in soup.find_all('div', {'class': 'col col1'}):
    title = div.find('span', {'class': 'title'}).text
    link = div.find('a', {'class': 'link_overlay'}).get('href')
    titles[title] = link
#To check what we've got,print
for t in titles.items():
    print(t)