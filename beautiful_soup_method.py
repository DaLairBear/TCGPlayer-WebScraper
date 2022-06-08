from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://shop.tcgplayer.com/price-guide/magic/commander-legends-battle-for-baldurs-gate').text
soup = BeautifulSoup(html_text, 'lxml')
cards = soup.find('div', class_ = 'productDetail')
card_page = cards.a['href']
print(card_page)