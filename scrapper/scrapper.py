import requests
from bs4 import BeautifulSoup

URL = "https://blasters4masters.com"
RESPONSE = requests.get(URL)
SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')


class Product:
    def __init__(self, name, price=-1, link="", desc=""):
        self.name = name
        self.price = price
        self.link = link
        self.desc = desc


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
    products = [Product]
    response = requests.get(category_url)
    category_soup = BeautifulSoup(response.text, 'html.parser')
    
    details = category_soup.find_all('div', attrs={'class':'text-center product-details'})

    products = [Product]
    
    for detail in details:
        h2_element = detail.find('h2')

        link = h2_element.find('a').get('href')
        detail_soup = BeautifulSoup(requests.get(link).text, "html.parser")
        desc = detail_soup.find('div', attrs={'class':'woocommerce-product-details__short-description'}).text.strip()
        name = h2_element.text.strip()
        price = detail.find('span').text.strip()

        product = Product(name=name, link=link, price=price, desc=desc)
        products.append(product)

        print(product.name + " | " + product.price + " | " + product.link + "\n" + product.desc + "\n")


    return products


if __name__ == "__main__":

    categories = get_categories(SOUP)

    for category in categories:
        print(f"Kategoria: {category['name']}")
        products = get_products(category['link'])
        for product in products:
            pass
            # print(f"Produkt: {product['name']}, Cena: {product['price']}")
