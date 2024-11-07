import env
from data_storage import *
from scrapper_modules.data_extraction import get_categories


def main():
    categories = get_categories()
    create_categories_directories(categories, env.SAVE_DIRECTORY)

    for category in categories:
        parent = category.parent_category
        parent_name = parent.name if parent is not None else "(none)"
        print(f"Kategoria: {category.name} <- {parent_name}")
        #products = get_products(category.link, category)

        #with open(save_path, 'w', encoding="utf-8") as file:
        #    for product in products:
        #        file.write(f"{product.to_csv()}\n")


if __name__ == "__main__":
    main()
