class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    specias = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    specias = 'feline'
    sounds = 'meow'

dog = Dog()
print(f'Dog is {dog.className}, but they say {dog.sounds}')
cat = Cat()
print(f'Cat is {cat.className}, but they say {cat.sounds}')