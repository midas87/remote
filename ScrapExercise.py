import requests
from bs4 import BeautifulSoup as bs

urlPage = requests.get('https://scrapingclub.com/exercise/list_basic/').text

soup = bs(urlPage, 'lxml')

items = soup.find_all('div', {'class': 'col-lg-4 col-md-6 mb-4'})

counter = 1

for name in items:
    clothType = name.find('h4', class_='card-title').a.text
    price = name.find('h5').text

    print(f'{counter}, ItemName: {clothType}, Amount: {price}')
    counter = counter + 1
# print(items)
