
import requests
from bs4 import BeautifulSoup

#using the wesite generally used for web scrapping 
url = "http://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'"{text}" - {author}')
