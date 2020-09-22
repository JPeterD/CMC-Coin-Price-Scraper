from bs4 import BeautifulSoup
import urllib2

coin = raw_input('What coin price are you looking for?\n')

url = 'https://coinmarketcap.com/currencies/'

final_url = ''.join([url, coin])

page = urllib2.urlopen(final_url)

soup = BeautifulSoup(page, 'html.parser')

price_find = soup.find('span', attrs={'class': 'cmc-details-panel-price__price'})

price = price_find.text.strip()

print price