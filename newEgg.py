import requests
from bs4 import BeautifulSoup

pageUrl = requests.get('https://www.newegg.com/p/pl?d=nas').text

# bb = requests.get('https://www.bestbuy.ca/en-ca/collection/headphones-on-sale/23058?icmp=pa_categorylanding_shopbycategory_audio_onsale').text

sp = BeautifulSoup(pageUrl, 'lxml')

nas = sp.find('div', {'class': 'item-cell'})
brandName = nas.find('div', {'class': 'item-branding'})
name = brandName.a.img['title']

prodSpec = nas.find('a', {'class': 'item-title'}).text

promo = nas.find('p', class_='item-promo').text

salesEnd = nas.find('span', {'class': 'price-save-endtime'}).text.replace('-', '')

print(name)
# print(brandName)
print(prodSpec)
print(promo)
print(salesEnd)

'''
# print(sp.prettify())

# dataContainers = sp.find_all('div', class_='item-container')


for container in dataContainers:
    print(container)
    if 'price' in container:

        sales = container.find_all('span', {'class': 'price-save-endtime'})
        print(sales)

    #salesEnd = sales.text

        #print(sales)

    #name = container.div.div.a.img['title']
    #print(name)

    #brandName = container.findAll('div', {'class': 'item-branding'})
    #name =
    #print(brandName['title'])

    #shipping = container = sp.find_all('li', {'class': 'price-ship'})

    #freeShip = shipping[0].text

    #link = container = sp.find_all('a', class_='item-title')
    # print(link)

    #productSpec = link[0].text
    # print(productSpec)

   # print(f'Brand :{name}, SalesEnd: {salesEnd}, FreeShipping: {freeShip}, Spec: {productSpec}')

'''
