from bs4 import BeautifulSoup
from requests import get

import requests
import urllib
import httplib2
import shutil

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url, stream=True, allow_redirects=False)
        print(response.headers)
        response.headers['Content-Type'] = 'text/srt'
        print(response.headers)
        print(response.status_code)
        # write to file
        file.write(response.content)
    # response = requests.get(url + ".srt", stream=True	)
    # response.headers['Content-Type'] = 'text/srt'	
    # with open('fucki', 'wb') as out_file:
    #     shutil.copyfileobj(response.raw, out_file)
    # del response
# tvs = input("Enter the TV series\n")
# tve= input("Enter the episode name\n")
# url="http://www.addic7ed.com/shows.php"

# r  = requests.get(url)

# data = r.text

# soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
#     if(link.text==tvs):
#     	tvurl=link.get('href')

tvurl = "/show/5346"
url="http://www.addic7ed.com"

r  = requests.get(url+tvurl)

data = r.text

soup = BeautifulSoup(data)

# allusers = []
# rows = soup.findAll('tr')
# for tr in rows:
#     cols = tr.findAll('td')
#     # print(type(cols))
    # for i in range(0, 10):
    # 	if(cols[i].text=="2"):
    # 		print(cols[i].findAll('a'))
    # for td in cols:
    #     if (td.text=="Download"):
    #     	print(cols[1].findAll('a'))

sea="1"
epi="5"
answer= ""
soup = BeautifulSoup(data)
tag = soup.findAll('td')
for i in range(7, 1000, 11):
	# print(tag[i].text)
	if(tag[i].text==sea and tag[i+1].text==epi):
		# print(tag[i].text)
		tag_a=tag[i+9].find('a')
		answer = tag_a['href']
		# print(tag_a['href'])
		break
		# print(tag[i+9].find('a')['href'])
# 
# 	tag_a = tag[9].find('a')
# tag_b = tag[31].find('a')
# print(tag_a.text + tag_b.text) #string 1
# print(tag_a['href'] + tag_b['href']) #/info/12345
download(url +answer, "abc")

# req = urllib.request.Request(url + answer, None)
# response = urllib.request.urlopen(req).read()
# with open("aaaaa.srt", "wb") as subtitle:
# subtitle.write(response)
# urltodownload = url+answer
# h = httplib2.Http()
# h.follow_redirects = False
# (response, body) = h.request(url+answer)
# print(body)
# print(response)