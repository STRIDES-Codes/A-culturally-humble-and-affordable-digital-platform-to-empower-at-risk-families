import requests
from bs4 import BeautifulSoup as bs
import json

search = input('Enter Search Item: ')
page_size = input('Enter page size: ')

url = 'https://www.yourindependentgrocer.ca/api/product/search/' + search +'?pageSize=' + page_size

payload = {'Host': 'www.yourindependentgrocer.ca',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en',
            'Accept-Encoding': 'gzip, deflate, br',
            'Site-Banner': 'independent',
            'Pickup-Location-Id': '1875',
            'Content-Type': 'application/json;charset=utf-8',
            'Connection': 'keep-alive',
            'Referer': 'https://www.yourindependentgrocer.ca/',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
}

print('Search Results: ')

r = requests.get(url=url, headers=payload)
data = r.json()
