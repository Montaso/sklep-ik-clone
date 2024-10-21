import Category


class Product:
    def __init__(self, name="", price=-1, link="", desc="", category: Category = None):
        self.name = name
        self.price = price
        self.link = link
        self.desc = desc
        self.category = category