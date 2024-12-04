import csv


class Category:
    def __init__(self, name: str, parent_category: object, link: str or None, description: str = ""):
        formatted_name = name.replace('/', '-')
        formatted_name = formatted_name.replace('\\', '-')

        self.parent_category = parent_category
        self.name = formatted_name
        self.link = link
        self.description = description
        self.added = False
        self.presta_id = None

    def __repr__(self):
        return f"\nCAT: {self.presta_id}, {self.parent_category}, {self.name}, {self.link}, {self.description}\n"

    def __str__(self):
        return self.name


def load_categories(filepath: str):
    categories = []
    first_id = 1
    with open(filepath, mode='r', ) as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            cat = Category(row['name'], row['parent_category'], row['link'], row['description'])
            categories.append(cat)

    # map to parents, add ids
    for cat in categories:
        if cat.parent_category == "None":
            cat.parent_category = None
            first_id += 1
        else:
            for cat2 in categories:
                if cat2.name == cat.parent_category:
                    cat.parent_category = cat2
                    break

    return categories
