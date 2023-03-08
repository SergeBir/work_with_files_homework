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

    def get_shop_list_by_dishes(self, dishes, person_count):
        with open("recipes.txt", "r") as file:
            cook_book = {}
            for line in file:
                name = line.strip()
                ingredient_count = int(file.readline())
                ingredients = {}
                for _ in range(ingredient_count):
                    products, quantity, measure = file.readline().strip().split(" | ")
                    ingredients[products] = {
                            "quantity": int(quantity) * person_count,
                            "measure": measure,
                        }
                cook_book[name] = ingredients
                file.readline()
            for name in cook_book.keys():
                if name in dishes:
                    pprint(cook_book[name])


new_work = WorkWithFiles()
new_work.files_manipulation()
new_work.get_shop_list_by_dishes(["Запеченный картофель", "Омлет"],2)
