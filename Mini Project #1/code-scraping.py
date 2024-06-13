from bs4 import BeautifulSoup
from datetime import date
import requests
import csv

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

df = []

for page_number in [1]:
    url = 'https://books.toscrape.com/catalogue/page-{}.html'.format(str(page_number))
    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, 'html.parser')

    data = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    
    for column in data:
        
        title = column.find('h3').find('a').get('title')

        price = column.find('p', class_="price_color").text.replace("Â","")

        rating = column.find('p').get('class')
        rating = rating[1]

        img = column.find('div', class_='image_container').find('img').get('src').replace('..','https://books.toscrape.com/')

        df += [[title,price,rating,img]]

column = ['Judul Buku','Harga Buku','Rating','Gambar Buku']

file = csv.writer(open('Mini Project #1\\hasil-scraping.csv','w',newline='',encoding='utf-8'))

file.writerow(column)

for item in df:
    file.writerow(item)