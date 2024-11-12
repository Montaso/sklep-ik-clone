import os

from models import Category


# supports only 'a' and 'w' open modes
def save(obj_arr: [object], save_path: str, open_mode='w'):
    if (open_mode == 'a' and not os.path.exists(save_path)) or open_mode == 'w':
        with open(save_path, open_mode, encoding="utf-8") as file:
            file.write(f"{get_csv_title_row(obj_arr[0])}\n")

    with open(save_path, 'a', encoding="utf-8") as file:
        for obj in obj_arr:
            file.write(f"{get_csv_value_row(obj)}\n")


def create_categories_directories(categories: [Category], root_path: str):
    for category in categories:
        new_dir_path = category.name
        p_cat = category.parent_category
        while p_cat is not None:
            new_dir_path = os.path.join(p_cat.name, new_dir_path)
            p_cat = p_cat.parent_category
        new_dir_path = os.path.join(root_path, new_dir_path)

        os.makedirs(new_dir_path, exist_ok=True)


def get_csv_value_row(obj: object) -> str:
    return ";".join("\"" + str(value).replace("\"", "\"\"") + "\"" for value in vars(obj).values())


def get_csv_title_row(obj: object) -> str:
    return ";".join(str(name) for name in vars(obj).keys())
