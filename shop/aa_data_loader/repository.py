from shop.aa_data_loader.models.category import load_categories, Category
from shop.aa_data_loader.send import send_get, send_post
import xml.etree.ElementTree as ET

from shop.aa_data_loader.xml_payloads import add_category_payload


def get_all_categories_ids():
    cat = send_get("categories").text
    root = ET.fromstring(cat)

    categories = root.findall(".//category")

    category_data = {}
    for category in categories:
        category_id = int(category.find('id').text)
        name_element = category.find("name/language")
        category_name = name_element.text.strip() if name_element is not None else None

        if category_name:
            category_data[category_name] = category_id

    categories_element = root.find("categories")
    categories = categories_element.findall('category')
    ids = []
    for category in categories:
        category_id = category.attrib['id']
        ids.append(int(category_id))
    return category_data


def add_all_categories(csv_path: str):
    cat = load_categories(csv_path)

    # add root
    for c in cat:
        if c.parent_category is None:
            add_category_to_prestashop(c)

    # add on depth=1
    for c in cat:
        if c.parent_category is not None and c.parent_category.added:
            add_category_to_prestashop(c)

    # add on depth=2
    for c in cat:
        if not c.added:
            add_category_to_prestashop(c)

    return cat


def add_category_to_prestashop(c: Category):
    parent_id = 2 if c.parent_category is None else c.parent_category.presta_id
    p = add_category_payload(parent_id, True, c.name, c.description, f"{c.name}-shop")
    response = send_post(p, "categories")
    c.added = True
    c.presta_id = get_id_from_response(response.text)


def get_id_from_response(response_text: str) -> int:
    root = ET.fromstring(response_text)
    return int(root.find(".//id").text.strip())
