from scrapper.models import Attribute, Category


class Product:
    def __init__(self,
                 name=None,
                 original_price=None,
                 new_price=None,
                 discount: int = -1,
                 link=None,
                 desc=None,
                 img_uris: [str] = None,
                 category: Category = None,
                 attributes: [Attribute] = None,
                 deal: str = ""
                 ):
        self.name = name
        self.original_price = original_price
        self.new_price = new_price
        self.link = link
        self.desc = desc
        self.category = category
        self.img_uris = img_uris
        self.attributes = attributes
        self.deal = deal
        self.discount = discount

    def __str__(self):
        return self.name
