# if in test, gets only one category
# and saves it in scrapper_test folder
ENV_TEST = True

# common
URL = "https://sklep-ik.pl"
IMG_SUBDIRECTORY_NAME = "img"
IMG_PER_PRODUCT = 2

# for test env
SAVE_DIRECTORY = "./data/test"
MAX_CATEGORIES = 100000

# for prod env
if not ENV_TEST:
    SAVE_DIRECTORY = "./data/prod"
    MAX_CATEGORIES = -1

# TODO: zaimplementować w scrapperze że img-per-prodcut = -1 to wszystkie zdjęcia
