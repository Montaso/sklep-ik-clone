import os

from models import Category


def save(obj_arr: [object], save_path: str, open_mode='w'):
    with open(save_path, open_mode, encoding="utf-8") as file:
        for product in obj_arr:
            file.write(f"{product.to_csv()}\n")


def create_categories_directories(categories: [Category], root_path: str):
    for category in categories:
        if category.parent_category is None:
            new_dir_path = os.path.join(root_path, category.name)
        else:
            new_dir_path = os.path.join(root_path, category.parent_category.name, category.name)
        os.makedirs(new_dir_path, exist_ok=True)


def get_csv_value_row(obj: object) -> str:
    return ";".join(str(value) for value in vars(obj).values())


def get_csv_title_row(obj: object) -> str:
    return ";".join(str(name) for name in vars(obj).keys())
