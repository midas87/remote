import requests
from bs4 import BeautifulSoup

# pageUrl = requests.get('https://www.newegg.com/p/pl?d=nas').text

bb = requests.get('https://www.bestbuy.ca/en-ca/collection/headphones-on-sale/23058?icmp=pa_categorylanding_shopbycategory_audio_onsale').text

sp = BeautifulSoup(bb, 'lxml')

print(sp.prettify())

'''
containers = sp.find_all('div', class_='productItemRow_hyNOs row_1mOdd')

container = containers[0]

print(container)
'''
