from pprint import pprint


class SecondWork:
    def __init__(self):
        pass

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


second_work = SecondWork()
second_work.get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)