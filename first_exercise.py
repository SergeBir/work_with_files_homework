from pprint import pprint


class FirstWork:
    def __init__(self):
        pass

    def show_data_in_files(self):
        with open("recipes.txt", "r") as file:
            cook_book = {}
            for line in file:
                name = line.strip()
                ingredient_count = int(file.readline())
                ingredients = []
                for _ in range(ingredient_count):
                    products, quantity, measure = file.readline().strip().split(" | ")
                    ingredients.append({
                        "ingredient_name": products,
                        "quantity": quantity,
                        "measure": measure,
                    })
                cook_book[name] = ingredients
                file.readline()
            for name, ingredients in cook_book.items():
                print(f"{name}:")
                pprint(ingredients, sort_dicts=False)


first_work = FirstWork()
first_work.show_data_in_files()
