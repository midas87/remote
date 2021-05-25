import requests
from bs4 import BeautifulSoup

urlPath = requests.get("https://www.linkedin.com/jobs/search/?alertAction=viewjobs&f_TPR=a1617761237-&keywords=system%20administrator&savedSearchId=1225646496&searchAlertRefId=9f02d6f5-f3fc-45dd-9217-da7d34a1d6c2").text

soup = BeautifulSoup(urlPath, 'lxml')

jobPage = soup.find_all('div', class_="relative")

print(jobPage)

