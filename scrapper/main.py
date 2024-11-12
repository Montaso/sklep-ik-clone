import env
from data_storage import *
from scrapper.scrapper_modules.products_extraction import get_products
from scrapper_modules.categories_extraction import get_categories


def main():
    categories = get_categories()
    create_categories_directories(categories, env.PATH_SAVE_DIRECTORY)
    save(categories, env.PATH_CATEGORIES_CSV)

    list_exported_categories(categories)
    for category in categories:
        pass
        products = get_products(category)

        #with open(save_path, 'w', encoding="utf-8") as file:
        #    for product in products:
        #        file.write(f"{product.to_csv()}\n")


def list_exported_categories(categories: [Category]):
    print("\n\nExported categories:")
    for category in categories:
        parent = category.parent_category
        parent_name = parent.name if parent is not None else "(none)"
        print(f"Kategoria: {category.name} <- {parent_name}")


if __name__ == "__main__":
    main()
