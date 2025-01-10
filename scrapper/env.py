import os

ENV_TEST = False

# for test env
PATH_SAVE_DIRECTORY = "data/test"
MAX_CATEGORIES = 1000000

# for prod env
if not ENV_TEST:
    PATH_SAVE_DIRECTORY = "data/prod"
    MAX_CATEGORIES = -1                     # -1 -> extract every category

# common
URL = "https://sklep-ik.pl"
IMG_SUBDIRECTORY_NAME = "img"
PATH_CATEGORIES_CSV = os.path.join(PATH_SAVE_DIRECTORY, "categories.csv")
PATH_PRODUCTS_CSV = os.path.join(PATH_SAVE_DIRECTORY, "products.csv")
IMG_PER_PRODUCT = 2

MAX_PRODUCTS_PER_CATEGORY = 10
ONLY_ONE_WOOL = False



