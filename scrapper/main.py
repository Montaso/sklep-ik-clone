import env
from data_storage import *
from scrapper_modules.products_extraction import get_products_in_category
from scrapper_modules.categories_extraction import get_categories, load_categories_from_csv


def main():
    categories = get_categories()
    # categories = load_categories_from_csv(env.PATH_CATEGORIES_CSV)

    list_exported_categories(categories)
    create_categories_directories(categories, env.PATH_SAVE_DIRECTORY)
    save(categories, env.PATH_CATEGORIES_CSV, 'w')

    for category in categories:
        # this ensures only one wool is downloaded - testing
        if (env.ONLY_ONE_WOOL
                and category.name != "ESTOŃSKA WEŁNA ARTYSTYCZNA 8-1"
                and ((category.parent_category is not None and category.parent_category.name == "Włóczki") or
                (category.parent_category is not None and category.parent_category.parent_category is not None
                and category.parent_category.parent_category.name == "Włóczki"))):
            print(f"skipping {category.name}")
            continue

        products = get_products_in_category(category)
        if products:
            save(products, env.PATH_PRODUCTS_CSV)


def list_exported_categories(categories: [Category]):
    print("\n\nExported categories:")
    for category in categories:
        parent = category.parent_category
        parent_name = parent.name if parent is not None else "(none)"
        print(f"Kategoria: {category.name} <- {parent_name}")


if __name__ == "__main__":
    main()
