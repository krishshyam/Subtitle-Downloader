from bs4 import BeautifulSoup
from requests import get

import requests
import urllib
import httplib2
import shutil
import os

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url, stream=True, allow_redirects=False)
        print(response.headers)
        response.headers['Content-Type'] = 'text/srt'
        print(response.headers)
        print(response.status_code)
        file.write(response.content)
tvs = input("Enter the TV series\n")
url="http://www.addic7ed.com/shows.php"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    if(link.text==tvs):
    	tvurl=link.get('href')

url="http://www.addic7ed.com"

r  = requests.get(url+tvurl)

data = r.text   
soup = BeautifulSoup(data)

sea=input("Enter the season")
epi=input("Enter the episode")
ver=input("Enter the version")
answer= ""
soup = BeautifulSoup(data)
tag = soup.findAll('td')
for i in range(7, 1000, 11):
    if(tag[i].text==sea and tag[i+1].text==epi and tag[i+3].text=="English" and tag[i+4].text==ver):
        tag_a=tag[i+9].find('a')
        answer = tag_a['href']
        break
os.system("start IDMan /d "+url+answer)