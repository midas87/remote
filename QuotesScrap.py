import requests
from bs4 import BeautifulSoup as bs

html_request = requests.get('https://quotes.toscrape.com/').text

soup = bs(html_request, 'lxml')

pageScrap = soup.find_all('div', {'class': 'quote'})
tag = soup.find_all('div', {'class': 'tags'})

fileQuote = open('Quotes.text', 'w')

for readLine in pageScrap:
    quote = readLine.find('span', class_='text').text

    author = readLine.find('small', {'class': 'author'}).text
    fileQuote.write(quote + '\n')
    fileQuote.write(author + '\n')

    for nameTag in tag:
        print(nameTag[a])
        #newTag = nameTag.find('a', {'class': 'tag'}).text
        #fileQuote.write(newTag + '\n')

fileQuote.close()
