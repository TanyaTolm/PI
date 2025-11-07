class Tanya:
    __slots__ = ['name']

    def __init__(self, name):
        if name == "Таня":
            self.name = f'Да, я {name}'
        else: self.name = f'Я не {name}, а Таня'

person1 = Tanya('Таня')
person2 = Tanya('Марина')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'