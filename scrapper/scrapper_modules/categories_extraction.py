import requests
from bs4 import BeautifulSoup, ResultSet, Tag
import scrapper.env as env
from scrapper.models.Category import Category


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
        parent = Category(name, None, None)
        append_with_communicate(parent, result_categories)

        subcategories = category.find_all('a', 'awb-menu__sub-a')
        for subcategory in subcategories:
            name = subcategory.find_next('span').get_text(strip=True)
            link = subcategory['href']
            new_subcategory = Category(name, parent, link)

            # skipping attribute-like subcategories
            if name == "Wszystkie Włóczki":
                break

            # cut first two and everything after 'WSZYSTKIE PROMOCJE',
            # because they are not categories
            if new_subcategory.name == 'WSZYSTKIE PROMOCJE':
                return result_categories[2:]

            append_with_communicate(new_subcategory, result_categories)

            if new_subcategory.parent_category.name == "Włóczki":
                result_categories.extend(extract_sub_subcategories(link, new_subcategory))

    return result_categories[2:]


def extract_sub_subcategories(subcategory_link: str, parent_category: Category):
    result_categories = []

    response = requests.get(subcategory_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    sub_subcategories_links = soup.find_all('a', 'fusion-column-anchor')[1:]
    sub_subcategories_text = soup.find_all('div', 'fusion-title-heading')

    text_iter = 0

    for sub_subcategory_link in sub_subcategories_links:
        if text_iter >= len(sub_subcategories_text):
            break

        name = sub_subcategories_text[text_iter].find_next('strong').get_text(strip=True)
        text_iter += 1
        link = sub_subcategory_link['href']
        description = sub_subcategories_text[text_iter].find_next('p').decode_contents()
        description = description.replace('\n', '')
        text_iter += 1

        new_subcategory = Category(name, parent_category, link, description)
        append_with_communicate(new_subcategory, result_categories)

    return result_categories


def append_with_communicate(category: Category, arr: [Category]):
    arr.append(category)
    print(f"Exported category: {category.name}")
