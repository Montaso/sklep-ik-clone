class Product:
    def __init__(self,
                 name=None,
                 original_price=None,
                 new_price=None,
                 discount: int = -1,
                 link=None,
                 desc=None,
                 img_uris: [str] = None,
                 category: str = None,
                 attributes: [str] = None,
                 deal: str = "",
                 advises: [str] = [],
                 weight: int = -1
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
        self.advises = advises
        self.weight = weight

    def __str__(self):
        return self.name