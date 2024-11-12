class Category:
    def __init__(self, name: str, parent_category: object, link: str or None, description: str = ""):
        formatted_name = name.replace('/', '-')
        formatted_name = formatted_name.replace('\\', '-')

        self.parent_category = parent_category
        self.name = formatted_name
        self.link = link
        self.description = description

    def __str__(self):
        return self.name
