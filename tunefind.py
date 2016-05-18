from bs4 import BeautifulSoup

import requests

ur1 = input("Enter the search\n")
#ur2 = input("Enter the Season\n")

url="http://www.stackoverflow.com/search?q="+ur1
r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))