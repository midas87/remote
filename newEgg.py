import requests
from bs4 import BeautifulSoup

pageUrl = requests.get('https://www.newegg.com/p/pl?d=nas').text

sp = BeautifulSoup(pageUrl, 'lxml')

nasDevices = sp.find_all('div', {'class': 'item-cell'})

for nas in nasDevices:

    promo = nas.find('p', class_='item-promo').text

    if 'promo' in promo:


        brandName = nas.find('div', {'class': 'item-branding'})
        name = brandName.a.img['title']

        prodSpec = nas.find('a', {'class': 'item-title'}).text

        #salesEnd = nas.find('span', {'class': 'price-save-endtime'}).text.replace('-', '')

        freeShip = nas.find('li', {'class': 'price-ship'}).text

        shipBy = nas.find('a', class_='shipped-by-newegg').text

        print(f'Brand: {name}, Specs: {prodSpec},  '
              f', FreeShipping : {freeShip}, ShipBy: {shipBy}''\n')



    #Promotion: {promo}
    #SalesEnding: {salesEnd}
    # print(name)
    # print(brandName)
    # print(prodSpec)
    #print(promo)
    # print(salesEnd)
    # print(freeShip)
    # print(shipBy)

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
