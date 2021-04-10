import requests
from bs4 import BeautifulSoup

# pageUrl = requests.get('https://www.newegg.com/p/pl?d=nas').text
pageDeals = requests.get('https://www.newegg.ca/DEALS-GALORE/EventSaleStore/ID-10468?utm_medium=Email&utm_source'
                         '=IGNEFL032421CA&nm_mc=EMC-IGNEFL032421CA&cm_mmc=EMC-IGNEFL032421CA-_-EMC-032421-Index-_-E0'
                         '-_-PromoWord&email64=aGFmZWV6dHVrdXJAaG90bWFpbC5jb20=&tp=i-1NGB-Q7E-4Lc-5ESAIU-2F-24hg-1c'
                         '-5ERwuA-l5r4LRbfXS-3QxQ&om_rid=494740&om_mid=16716').text

sp = BeautifulSoup(pageDeals, 'lxml')

word = sp.div

for n in sp.find_all('option'):
    print(n.string)

# print(word)
