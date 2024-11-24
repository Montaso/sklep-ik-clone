# pobiera zdjecia i zwraca tablice ze sciezkami do plikow
import os
import requests
from bs4 import BeautifulSoup
import re
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

    product_name = soup.find('div', class_='fusion-title-2').get_text(strip=True)

    product_current_price = None
    product_original_price = None
    product_price_text = soup.find('p', attrs={'class': 'price'}).get_text(strip=True)

    # sprawdzenie czy to zwykła cena
    price_match = re.match(r'([\d,]+zł)', product_price_text)
    if price_match:
        product_current_price = (price_match.group(1))
    else:
        # sprawdzenie czy to zakres cen
        range_match = re.match(r'([\d,]+zł)–([\d,]+zł)', product_price_text)
        if range_match:
            product_current_price = (range_match.group(1), range_match.group(2))
        
        else:
            # sprawdzenie czy to cena przeceniona
            discount_match = re.search(r'Original price was:\s*([\d,]+)\s*zł.*?Current price is:\s*([\d,]+)\s*zł', 
            product_price_text.replace('\xa0', ' ')
            )
            if discount_match:
                product_original_price = discount_match.group(1) + "zł"
                product_current_price = discount_match.group(2) + "zł"
        

    product_desc_meta_tag = soup.find('meta', attrs={'name': 'description'})
    product_desc = None
    # opis produktu jest w atrybucie content w tagu <meta>
    if product_desc_meta_tag and 'content' in product_desc_meta_tag.attrs:
        product_desc = product_desc_meta_tag['content'].strip()

    # zdjecia produktu
    product_image_a = soup.find_all('a', attrs={'class': 'avada-product-gallery-lightbox-trigger'})
    product_uris = []
    if product_image_a:
        for a_tag in product_image_a:
            if 'href' in a_tag.attrs:
                product_uris.append(a_tag['href'])

    # atrybuty produktu (tuple z tytułem atrybutu i jego opisem)
    attributes_table = soup.find('table', class_='woocommerce-product-attributes shop_attributes')
    product_attributes = []
    if attributes_table:
        rows = attributes_table.find_all('tr')
        for row in rows:
            label = row.find('th').text.strip()
            value = row.find('td').text.strip()
            product_attributes.append((label, value))

    #TODO Dodac reszte atrybutow produktu (deal, discount, advises, weight)

    return Product(name= product_name, original_price=product_original_price, new_price=product_current_price, link=products_subpage_url, desc=product_desc, img_uris=product_uris, category=products_category, attributes=product_attributes)


# funkcja pobiera dane o wszystkich produktach w kategorii (ich nazwę i cenę)
def get_products_in_category(category: Category) -> [Product]:
    if category.link is None:
        return []

    result_products: [Product] = []

    response = requests.get(category.link)
    category_soup = BeautifulSoup(response.text, 'html.parser')

    products_div = category_soup.find_all('div', attrs={'class': 'product-details-container'})

    for div in products_div:
        try:
            # znajdywanie linku w kontenerze produktu
            a_tag = div.find('a')
            if a_tag and 'href' in a_tag.attrs:
                product_link = a_tag['href']
                product = extract_product(product_link, category)
                append_with_communicate(product, result_products)
                result_products.append(product)
        except Exception as e:
            print("Can't extract product: ", e, "\nURL:\n", product_link)

    return result_products


def append_with_communicate(product: Product, arr: [Product]):
    arr.append(product)
    print(f"Exported product: {product.name} (category: {product.category})\n\toriginal_price: {product.original_price} new_price: {product.new_price}")
