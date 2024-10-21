import requests
from bs4 import BeautifulSoup

url = "https://blasters4masters.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# funkcja ściąga wszystkie kategorie ze stronyi zapisuje ich nazwy + linki
def get_categories(soup):
    categories = []
    for category in soup.find_all('li', class_='cat-item'):
        name = category.get_text(strip=True)
        link = category.find('a')['href']
        categories.append({
            'name': name,
            'link': link
        })
    return categories

# TODO iterować po kolejnych podstronach kategorii (bo na razie bierze tylko z page 1 kategorii)
# funkcja pobiera dane o wszystkich produktach w kategorii (ich nazwę i cenę)
def get_products(category_url):
    products = []
    response = requests.get(category_url)
    category_soup = BeautifulSoup(response.text, 'html.parser')

    for product in category_soup.find_all('div', class_='content-product'):
        name = product.select_one('.product-title').text.strip()
        price = product.select_one('.price').text.strip()

        products.append({
            'name': name,
            'price': price
        })
    return products

categories = get_categories(soup)

for category in categories:
    print(f"Kategoria: {category['name']}")
    products = get_products(category['link'])
    for product in products:
        print(f"Produkt: {product['name']}, Cena: {product['price']}")
