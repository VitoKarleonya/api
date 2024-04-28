import requests
from bs4 import BeautifulSoup

url = "https://www.afi.com/afis-100-years-100-movies/";
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 '
'Firefox/50.0'})

soup = BeautifulSoup(req.content, 'html.parser')
films = soup.find_all('h6', {'class': 'q_title'})
print([film.text for film in films])