class Russian:
    @staticmethod
    def greeting(): print("Привет")

class English:
        @staticmethod
        def greeting(): print('Hello')

def greet(lenguage):
    lenguage.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)