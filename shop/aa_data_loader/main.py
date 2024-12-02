import csv

from shop.aa_data_loader.Product import Product
from xml_payloads import *
from send import send, get_blank_schema

# payload = add_category_payload(2, 1, "test_name", "test_desc", "test_link")
# send(payload, "categories")

PATH_PRODUCTS_CSV = '../../scrapper/data/test/products.csv'
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
        print(product)

for product in products:
    default_category_id = 999999 # unknown yet
    new_price = product.new_price
    active = True # czy produkt jest dostępny
    name = product.name
    url = product.link
    desc = product.desc
    short_desc = '???' # i dont know what to put here
    category_id = 999999 # unknown yet
    state = 1 # no info
    img_uris = product.img_uris

    payload = add_product_payload(default_category_id, new_price, active, name,
                                  url, desc, short_desc, category_id, state)
    send(payload, "products", img_uris)
    break



