from bs4 import BeautifulSoup
import requests
if __name__=="__main__":
  req = requests.get("http://www.saavn.com/s/featured/hindi/Weekly_Top_Songs/8MT-LQlP35c_")
  data = req.text
  soup=BeautifulSoup(data,"html.parser")
  for i in soup.find_all('span',{'class':'title'}):
    print i.find('a').text
