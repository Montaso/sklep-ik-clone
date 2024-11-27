class Attribute:
    def __init__(self,
                 attr_name: str = "",
                 attr_value: str = ""
                 ):
        self.name = attr_name
        self.value = attr_value

    def __str__(self):
        return self.name
