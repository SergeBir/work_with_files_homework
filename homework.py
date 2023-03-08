from pprint import pprint


class WorkWithFiles:
    def __init__(self):
        pass

    def files_manipulation(self):
        with open("recipes.txt", "r") as file:
            cook_book = {}
            for line in file:
                name = line.strip()
                ingredient_count = int(file.readline())
                ingredients = []
                for _ in range(ingredient_count):
                    products, count, size_form = file.readline().strip().split(" | ")
                    ingredients.append({
                        "ingredient_name": products,
                        "quantity": count,
                        "measure": size_form,
                    })
                cook_book[name] = ingredients
                file.readline()
            for name, ingredients in cook_book.items():
                print(f"{name}:")
                pprint(ingredients, sort_dicts=False)



new_work = WorkWithFiles()
new_work.files_manipulation()
