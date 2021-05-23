import requests
from bs4 import BeautifulSoup as bs

webPage = requests.get('https://ca.indeed.com/jobs?q=linux+system+administrator&l=Mississauga%2C+ON').text

soup = bs(webPage, 'lxml')

# print(soup)

jobSearch = soup.find_all('span', {'class': 'new'})

for i in jobSearch:
    datePosted = i.find('span', {'class': 'date date-a11y'})
    print(datePosted)

# print(jobSearch)
