import requests
from Product import Product
from Category import Category
from bs4 import BeautifulSoup

URL = "https://blasters4masters.com"
RESPONSE = requests.get(URL)
SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')


# funkcja ściąga wszystkie kategorie ze stronyi zapisuje ich nazwy + linki
def get_categories(soup):
    categories = [Category]
    for category in soup.find_all('li', class_='cat-item'):
        name = category.get_text(strip=True)
        link = category.find('a')['href']
        categories.append({
            new Category
        })
    return categories


def extract_product(source):
    h2_element = source.find('h2')

    name = h2_element.text.strip()
    price = source.find('span').text.strip()
    link = h2_element.find('a').get('href')

    desc = None
    detail_soup = BeautifulSoup(requests.get(link).text, "html.parser")
    desc_element = detail_soup.find('div', attrs={'class': 'woocommerce-product-details__short-description'})
    if desc_element is not None:
        desc_text = desc_element.text
        if desc_text is not None:
            desc = desc_text.strip()

    return Product(name=name, link=link, price=price, desc=desc)


# TODO iterować po kolejnych podstronach kategorii (bo na razie bierze tylko z page 1 kategorii)
# funkcja pobiera dane o wszystkich produktach w kategorii (ich nazwę i cenę)
def get_products(category_url):
    response = requests.get(category_url)
    category_soup = BeautifulSoup(response.text, 'html.parser')
    
    details = category_soup.find_all('div', attrs={'class': 'text-center product-details'})

    products = [Product]
    
    for detail in details:
        product = extract_product(detail)
        products.append(product)
        print(product.name + " | " + product.price + " | " + product.link + "\n" + product.desc + "\n")

    return products


def main():
    categories = get_categories(SOUP)

    for category in categories:
        print(f"Kategoria: {category['name']}")
        products = get_products(category['link'])
        for product in products:
            pass
            # print(f"Produkt: {product['name']}, Cena: {product['price']}")


if __name__ == "__main__":
    main()
