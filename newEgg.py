import requests
from bs4 import BeautifulSoup

pageUrl = requests.get('https://www.newegg.com/p/pl?d=nas').text

# bb = requests.get('https://www.bestbuy.ca/en-ca/collection/headphones-on-sale/23058?icmp=pa_categorylanding_shopbycategory_audio_onsale').text

sp = BeautifulSoup(pageUrl, 'lxml')

# print(sp.prettify())

dataContainers = sp.find_all('div', class_='item-container')


for container in dataContainers:

    # container = containers[0]

    #n = container.div.div.a.img['title']

    sales = dataContainers = sp.find_all('span', {'class': 'price-save-endtime'})

    salesEnd = sales[0].text

    shipping = container = sp.find_all('li', {'class': 'price-ship'})

    freeShip = shipping[0].text

    link = container = sp.find_all('a', class_='item-title')

    productName = link[0].text

    #site = container.a['href']

# print(link)

print(freeShip)

#print(n)

# print(sales)

print(salesEnd)

print(productName)

#print(site)
