class House:
    houses_history = []  # Атрибут класса для хранения истории зданий

    def __new__(cls, name, number_of_floors):
        # Создаем новый объект
        instance = super(House, cls).__new__(cls)
        # Добавляем название здания в историю
        cls.houses_history.append(name)
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

