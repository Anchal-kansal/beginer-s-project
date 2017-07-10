from bs4 import BeautifulSoup
import requests
import os
x=int(input())
y=int(input())
for comic in range(x,y+1):
    img=str(comic)
    url="https://xkcd.com/"
    url+=img+"/"
    r=requests.get(url)
    data=r.text
    soup=BeautifulSoup(data,"html.parser")
    for i in soup.find_all('img'):
      dl=i.get('src')
      os.system ("wget "+"http:"+dl)
      
