import Category
import Attribute


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

    def to_csv(self):
        return f"{self.name};{self.price};{self.link};{self.desc};{self.category};{self.img_uris};{self.attributes}"