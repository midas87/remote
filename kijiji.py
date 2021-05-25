from bs4 import BeautifulSoup
import requests

html_url = requests.get('https://www.kijiji.ca/b-cars-trucks/gta-greater-toronto-area/toyota-sienna-used/c174l1700272a54a1000054a49').text
#print(html_url.text)

#html_url = requests.get("https://www.linkedin.com/jobs/")
#print(html_url)

soup = BeautifulSoup(html_url, 'lxml')
niceFile = soup.text
#price = soup.find_all('li', class_ = 'highlight' )

#priceFrom = soup.find_all('')

#price_name = price.find('h3')

#print(price)
#print(price_name)

with open(soup) as f:
    f.write("newFile.txt")

print('Done')

