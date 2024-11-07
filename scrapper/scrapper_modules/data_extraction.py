import os
import requests
from bs4 import BeautifulSoup
import scrapper.env as env
from scrapper.models.Category import Category
from scrapper.models.Product import Product


# funkcja ściąga wszystkie kategorie ze strony i zapisuje ich nazwy + linki do podstron
def get_categories() -> [Category]:
    result_categories: [Category] = []

    response = requests.get(env.URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories_html = soup.find_all('li', class_='awb-menu__main-li')

    if env.MAX_CATEGORIES != -1:
        max_categories = min(env.MAX_CATEGORIES, len(categories_html) - 1)
        categories_html = categories_html[:max_categories]

    for category in categories_html:
        name_span = category.find_next('span', class_='menu-text')
        name = name_span.get_text(strip=True)
        parent = Category(name, None, None, None)
        result_categories.append(parent)

        subcategories = category.find_all('a', 'awb-menu__sub-a')
        for subcategory in subcategories:
            name = subcategory.find_next('span').get_text(strip=True)
            link = subcategory['href']
            new_subcategory = Category(name, parent, link, None)
            result_categories.append(new_subcategory)

            # cut first two and everything after 'WSZYSTKIE PROMOCJE',
            # because they are not categories
            if new_subcategory.name == 'WSZYSTKIE PROMOCJE':
                return result_categories[2:]

    return result_categories[2:]


# pobiera zdjecia i zwraca tablice ze sciezkami do plikow
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


# TODO: dodać kategorię i atrybuty
# tworzy instację Product z odpowiedniego fragmentu html
def extract_product(source, category: Category) -> Product:
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

    imgs = get_imgs(detail_soup, name, category.name)

    return Product(
        name=name,
        link=link,
        price=price,
        desc=desc,
        img_uris=imgs
    )


# TODO iterować po kolejnych podstronach kategorii (bo na razie bierze tylko z page 1 kategorii)
# funkcja pobiera dane o wszystkich produktach w kategorii (ich nazwę i cenę)
def get_products(category_url: str, category: Category) -> [Product]:
    result_products: [Product] = []

    response = requests.get(category_url)
    category_soup = BeautifulSoup(response.text, 'html.parser')

    products_details = category_soup.find_all('div', attrs={'class': 'text-center product-details'})

    for detail in products_details:
        try:
            product = extract_product(detail, category)
            result_products.append(product)
            print(product.name + " | " + product.price + " | " + product.link + "\n" + product.desc + "\n")
        except Exception as e:
            print("Can't extract product: ", e, "\nHTML fragment:\n", detail)

    return result_products