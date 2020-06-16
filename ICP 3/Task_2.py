import requests
from bs4 import BeautifulSoup

url = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
htmltext = url.text
soup = BeautifulSoup(htmltext, 'html.parser')
title = soup.find('title')
#used to print title
print(title.string)
#print all link in a given page
a = soup.findAll('a')
print(a)
# print all the links which contain "href" tag
f=open("output.txt","w")
for i in a:
    link= i.get("href")
    if link != None:
        f.write(link)
        f.write("\n")
    else:
        continue
f.close()


