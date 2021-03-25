import requests
from bs4 import BeautifulSoup

pageUrl = requests.get('https://www.newegg.com/p/pl?d=nas').text


sp = BeautifulSoup(pageUrl, 'lxml')

lb = sp.find_all('option')

for n in lb:
    ckPrice = n.attrs
    print(ckPrice['value'])
    if int(ckPrice['value']) == 1:
        nPage = requests.get('https://www.newegg.com/p/pl?d=nas&recaptcha=pass&Order=1').text
        nwPage = BeautifulSoup(nPage, 'lxml')
        print(nwPage('a'))
        break




#print(lb)
#print(sp.prettify())
