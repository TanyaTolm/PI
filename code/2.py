class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else: self.ingredient = None

    def composion(self):
        if self.ingredient:
            print(f'Мороженое с {self.ingredient}')
        else: print('Обычное мороженое')

icecream = Icecream()
icecream.composion()
icecream = Icecream("шоколадом")
icecream.composion()
icecream = Icecream(5)
icecream.composion()