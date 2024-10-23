import os

import requests
import env
from Product import Product
from Category import Category
from bs4 import BeautifulSoup


# TODO: wymyslić jak robimy podkategorie i poprawnie je mapować jako parent category
# funkcja ściąga wszystkie kategorie ze strony i zapisuje ich nazwy + linki
def get_categories() -> [Category]:
    result_categories: [Category] = []

    response = requests.get(env.URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories_html = soup.find_all('li', class_='cat-item')

    if env.ENV_TEST:
        categories_html = [categories_html[0]]

    for category in categories_html:
        name = category.get_text(strip=True)
        link = category.find('a')['href']
        result_categories.append(Category(name, None, link))

    return result_categories


# pobiera zdjecia i zwraca tablice ze sciezkami do plikow
def get_imgs(soup: BeautifulSoup) -> [str]:
    save_path = env.TEST_IMG_SAVE_PATH if env.ENV_TEST else env.PROD_IMG_SAVE_PATH
    max_img_num = env.TEST_IMG_PER_PRODUCT if env.ENV_TEST else env.PROD_IMG_PER_PRODUCT
    os.makedirs(save_path, exist_ok=True)

    img_divs = soup.find_all('div', class_='woocommerce-product-gallery__image')
    uri_array = []
    i = 0

    try:
        for div in img_divs:
            if i >= max_img_num:
                break
            i += 1

            url = div.find('a')['href']
            img_name = url.split('/')[-1]
            uri = os.path.join(save_path, img_name)

            response = requests.get(url)
            with open(uri, 'wb') as file:
                file.write(response.content)

            uri_array.append(uri)

    # czyści śmieci jeżeli coś się wykręciło
    except Exception as ex:
        for uri in uri_array:
            if os.path.exists(uri):
                os.remove(uri)
        raise

    return uri_array


# TODO: dodać kategorię i atrybuty
# tworzy instację Product z odpowiedniego fragmentu html
def extract_product(source) -> Product:
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

    imgs = get_imgs(detail_soup)

    return Product(
        name=name,
        link=link,
        price=price,
        desc=desc,
        img_uris=imgs
    )


# TODO iterować po kolejnych podstronach kategorii (bo na razie bierze tylko z page 1 kategorii)
# funkcja pobiera dane o wszystkich produktach w kategorii (ich nazwę i cenę)
def get_products(category_url) -> [Product]:
    result_products: [Product] = []

    response = requests.get(category_url)
    category_soup = BeautifulSoup(response.text, 'html.parser')
    
    products_details = category_soup.find_all('div', attrs={'class': 'text-center product-details'})

    for detail in products_details:
        try:
            product = extract_product(detail)
            result_products.append(product)
            print(product.name + " | " + product.price + " | " + product.link + "\n" + product.desc + "\n")
        except Exception as e:
            print("Can't extract product: ", e, "\nHTML fragment:\n", detail)

    return result_products


def main():
    categories = get_categories()
    save_path = env.TEST_CSV_SAVE_PATH if env.ENV_TEST else env.PROD_IMG_SAVE_PATH
    # os.makedirs(save_path, exist_ok=True)

    for category in categories:
        print(f"Kategoria: {category.name}")
        products = get_products(category.link)

        with open(save_path, 'w', encoding="utf-8") as file:
            for product in products:
                file.write(f"{product.to_csv()}\n")


if __name__ == "__main__":
    main()
