from bs4 import BeautifulSoup
import requests
url = requests.get("https://en.wikipedia.org/wiki/Google")
#gets the html text
htmltext = url.text
soup = BeautifulSoup(htmltext, 'html.parser')
p = soup.findAll('p')
f=open("input.txt","w")
for i in p:
    x= i.get_text()
    if x!="":
        f.write(x)