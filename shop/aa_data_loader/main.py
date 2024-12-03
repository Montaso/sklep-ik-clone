import csv
import random

import requests

from shop.aa_data_loader.Product import Product
from xml_payloads import *
import send
import repository
import xml.etree.ElementTree as ET

SEND_CATEGORIES = True
UPLOAD_IMAGES = False
PATH_PRODUCTS_CSV = '../../data/prod/products.csv'

def add_categories_to_shop():
    repository.add_all_categories(PATH_PRODUCTS_CSV)


def get_all_products():
    products = []
    with (open(PATH_PRODUCTS_CSV, mode='r', encoding='utf-8') as csv_file):
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            if row.get('new_price')[0] == '(':
                continue
            if row.get('discount').strip() == 'Non' or row.get('discount').strip() == 'None':
                continue
            if row.get('weight').strip() == 'Non' or row.get('weight').strip() == 'None':
                continue

            new_price = float(row.get('new_price')[:-2].replace(",", "."))
            product = Product(
                name=row.get('name'),
                original_price=row.get('original_price'),
                new_price=new_price,
                discount=int(row.get('discount', -1)[:-1]),
                link=row.get('link'),
                desc=row.get('desc'),
                img_uris=row.get('img_uris', '').split(','),  # Assuming image URIs are comma-separated
                category=row.get('category'),
                attributes=row.get('attributes', '').split(','),  # Assuming attributes are comma-separated
                deal=row.get('deal', ""),
                advises=row.get('advises', '').split(','),  # Assuming advises are comma-separated
                weight=int(row.get('weight', -1)[:-1])
            )
            products.append(product)
    return products


def update_stock(stock_id, quantity):
    stock_url = f'{send.base_url}stock_availables/{stock_id}'
    response = requests.get(
        stock_url,
        auth=(send.api_key, ''),
        verify=False
    )

    if response.status_code == 200:
        print(f"Successfully fetched stock XML for stock ID {stock_id}")
    else:
        print(f"Failed to fetch stock XML for stock ID {stock_id}. Status code: {response.status_code}")
        return None

    root = ET.fromstring(response.text)
    quantity_element = root.find(".//stock_available/quantity")
    if quantity_element is not None:
        quantity_element.text = str(quantity)
    payload = ET.tostring(root, encoding='utf-8')

    response = requests.put(
        f'{send.base_url}stock_availables/{stock_id}',
        auth=(send.api_key, ''),
        headers={'Content-Type': 'application/xml'},
        data=payload,
        verify=False
    )

    if response.status_code == 200:
        print(f"Stock updated successfully for stock ID {stock_id}.")
    else:
        print(f"Failed to update stock for stock ID {stock_id}. Status code: {response.status_code}")


def get_product_id(response):
    root = ET.fromstring(response.text)
    product_id = int(root.find(".//id").text)
    return product_id


def get_stock_id(product_id):
    stock_url = f"{send.base_url}stock_availables?filter[id_product]={product_id}"
    response = requests.get(
        stock_url,
        auth=(send.api_key, ''),
        verify=False
    )

    if response.status_code == 200:
        root = ET.fromstring(response.text)
        stock_available_element = root.find(".//stock_available")
        if stock_available_element is not None:
            stock_id = stock_available_element.get("id")
            if stock_id:
                return int(stock_id)
        print("No stock ID found in the response. Check the XML structure.")
    else:
        print(f"Failed to retrieve stock ID for product ID {product_id}. Status code: {response.status_code}")
    return None


def add_products_to_shop(products: list[Product], categories: dict[str:int]):
    for product in products:
        default_category_id = categories[product.category]
        new_price = product.new_price
        active = True  # czy produkt jest dostępny
        name = product.name
        url = product.link
        desc = product.desc
        category_id = categories[product.category]
        state = 1
        img_uris = product.img_uris
        quantity = random.randint(1, 20)
        weight = product.weight

        payload = add_product_payload(default_category_id, new_price, active, name,
                                      url, desc, category_id, state,
                                      weight)
        response = send.send(payload, "products")

        if response.status_code == 201:
            print('added product succesfully')
        else:
            print('failed to add product')

        if response:
            product_id = get_product_id(response)
            update_stock(get_stock_id(product_id), quantity)

            if UPLOAD_IMAGES:
                send.upload_product_images(product_id, img_uris)




def main():
    if SEND_CATEGORIES:
        add_categories_to_shop()

    categories = repository.get_all_categories_ids()
    products = get_all_products()
    add_products_to_shop(products, categories)






if __name__ == '__main__':
    main()


