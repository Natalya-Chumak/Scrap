import requests
from bs4 import BeautifulSoup


url = 'https://vc.ru/marketing/632911-onlayn-kvest-dlya-podpischikov-vk-i-midjouney-kotoryy-nam-ego-otrisoval'
response = requests.get(url)
soup = BeautifulSoup(response.text)
# print(soup)

quotes = soup.find_all('div', class_="l-island-a")          #, class_='text'

print(quotes)
for quote in quotes:
    print(quote.text)
