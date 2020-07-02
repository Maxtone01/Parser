from bs4 import BeautifulSoup
import requests
import csv

URL = 'https://www.olx.ua/kiev/q-playstation-4-slim/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
FILE = 'results.csv'

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'Ссылка'])
        for item in items:
            writer.writerow([item['Title'], item['Price'], item['Link']])

def parse():
    r = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(r.content, 'html.parser')
    items = soup.findAll('div', class_='offer-wrapper')
    results = []

    for item in items:
        results.append({
            'Title': item.find('a', class_='marginright5 link linkWithHash detailsLink').get_text(strip=True),
            'Price': item.find('p', class_='price').get_text(strip=True),
            'Link': item.find('a', class_='marginright5 link linkWithHash detailsLink').get('href')
        })
    save_file(results, FILE)
parse()