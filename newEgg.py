import requests
from bs4 import BeautifulSoup

pageUrl = requests.get('https://www.newegg.com/p/pl?d=nas').text

'''
soup = BeautifulSoup(pageUrl, 'lxml')

niceFile = soup.find_all('a', class_='item-title')

for n in niceFile:
    opt = 

'''

sp = BeautifulSoup(pageUrl, 'lxml')

print(sp.prettify())
