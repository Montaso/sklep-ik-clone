# pobiera zdjecia i zwraca tablice ze sciezkami do plikow
import os
import requests
from bs4 import BeautifulSoup
from scrapper import env
from scrapper.models.Category import Category
from scrapper.models.Product import Product


# !!!! metoda nie działa w sklep-ik, stworzona dla blasters4masters
def get_imgs(soup: BeautifulSoup, product_name: str, category_name: str) -> [str]:
    save_path = env.TEST_IMG_SAVE_PATH if env.ENV_TEST else env.PROD_IMG_SAVE_PATH
    save_path = os.path.join(save_path, category_name, product_name)
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
    except Exception:
        for uri in uri_array:
            if os.path.exists(uri):
                os.remove(uri)
        raise

    return uri_array


# tworzy instację Product z odpowiedniego fragmentu html
def extract_product(products_subpage_url: str, products_category: Category) -> Product:
    response = requests.get(products_subpage_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return Product()


# funkcja pobiera dane o wszystkich produktach w kategorii (ich nazwę i cenę)
def get_products_in_category(category: Category) -> [Product]:
    if category.link is None:
        return []

    result_products: [Product] = []

    response = requests.get(category.link)
    category_soup = BeautifulSoup(response.text, 'html.parser')

    products_details_urls = category_soup.find_all('div', attrs={'class': 'fusion-link-wrapper'})

    for detail_url in products_details_urls:
        try:
            product = extract_product(detail_url, category)
            append_with_communicate(product, result_products)
        except Exception as e:
            print("Can't extract product: ", e, "\nURL:\n", products_details_urls)

    return result_products


def append_with_communicate(product: Product, arr: [Product]):
    arr.append(product)
    print(f"Exported product: {product.name} (category: {product.category})")
