from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/')
html = url.content
# print(html)

soup = BeautifulSoup(html, 'html.parser')
books_block = soup.select('section')
block = books_block[0]
books_full = block.select_one('ol', class_='row')
books = books_full.select('li')

data_base = []

for i in books:
    image = 'https://books.toscrape.com/' + i.find('div', class_='image_container').find('img')['src']
    title = i.find('h3').find('a')['title']
    price = i.find('div', class_="product_price").find('p', class_="price_color").text

    book_dict = {
        'image': image,
        'title': title,
        'price': price
    }

    data_base.append(book_dict)
print(data_base[19])

