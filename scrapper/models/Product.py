from scrapper.models import Attribute, Category


class Product:
    def __init__(self,
                 name="",
                 price=-1,
                 link="",
                 desc="",
                 img_uris: [str] = [],
                 category: Category = None,
                 attributes: [Attribute] = []
                 ):
        self.name = name
        self.price = price
        self.link = link
        self.desc = desc
        self.category = category
        self.img_uris = img_uris
        self.attributes = attributes

    def __str__(self):
        return self.name
