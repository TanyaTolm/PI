class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    """
    Инициализация объекта Tomato.
    index (int): Индекс томата.
    state (int): Текущее состояние томата.
    """

    # Переводит томат на следующую стадию созревания
    def grow(self):
        self._state += 1

    # Проверяет созрел ли томат
    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index) for index in range(0, tomato_count)]

    """
    Инициализация объекта TomatoBush.
    tomato_count (int): Количество томатов на кусте.
    tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
    """

    # Переводит все томаты на кусте на слудющую стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяет все ли томаты на кусте созрели
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Собирает урожай с куста
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
            self.name = name
            self._plant = plant

    """
    Инициализация объекта Gardener.
    name (str): Имя садовника.
    plant(TomatoBush): Куст томатов, за которым ухаживает садовник.
    """

    # Садовник работает, переводя томаты на следующую стадию созревания
    def work(self):
        self._plant.grow_all()
        print("Ухаживаем за растениями")

    # Проверяет созрели ли все томаты на кусте и собирает, если пора
    def harvaest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
        else: print("Томаты ещё не созрели")

    # Справка о порядке действий по уходу за томатами
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: \n" 
                "1. Посадить куст томатов\n"
                "2. Назначить садовника на куст\n"
                "3. Ухаживать за кустом\n"
                "4. Собрать урожай")

a = TomatoBush(5)
b = Gardener("Tanya", a)