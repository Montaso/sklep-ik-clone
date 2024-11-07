class Category:
    def __init__(self, name: str, parent_category: object, link: str or None, dir_path: str):
        self.parent_category = parent_category
        self.name = name
        self.link = link
        self.products = []
        self.directory_path = dir_path

    def __str__(self):
        return self.name
