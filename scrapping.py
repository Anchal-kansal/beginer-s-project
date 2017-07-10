from bs4 import BeautifulSoup

import sys

import requests



url1="http://www.imdb.com/india/top-rated-indian-movies"

re =  requests.get(url1)

print re



c = re.text



soup = BeautifulSoup(c, "html.parser")

for i in soup.findAll('td',{'class': 'titleColumn'}):

    name=i.find('a').text

    print name
