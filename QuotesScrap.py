import requests

from bs4 import BeautifulSoup as bs

html_request = requests.get('https://quotes.toscrape.com/').text

soup = bs(html_request, 'lxml')

pageScrap = soup.find_all('div', {'class': 'quote'})

fileQuote = open('Quotes.text', 'w')

for readLine in pageScrap:
    quote = readLine.find('span', class_='text').text

    author = readLine.find('small', {'class': 'author'}).text

    fileQuote.write(quote + '\n')
    fileQuote.write(author + '\n')

fileQuote.close()
