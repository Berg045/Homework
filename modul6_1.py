# class Animal:
#     def __init__(self, name):
#         self.alive = True
#         self.fed = False
#         self.name = name
#
# class Plant:
#    def __init__(self, name):
#        self.edible = False
#        self.name = name
#
# class Mammal(Animal):
#     def eat(self, food):
#         if isinstance(food, Fruit):
#             self.fed = True
#             print('Хатико съел Заводной апельсин')
#         else:
#             print('Я не могу съесть это')
#
# class Predator(Animal):
#     def eat(self, food):
#         if isinstance(food, Fruit):
#             self.fed = False
#             print('Я съел фрукт')
#         else:
#             print('Волк с Уолл-Стрит не стал есть Цветик семицветик')
#             self.alive = False
#
# class Flower(Plant):
#     def eat(self, food):
#         if isinstance(food, Fruit):
#             self.fed = True
#
# class Fruit(Plant):
#     def eat(self, food):
#         if isinstance(food, Fruit):
#             self.edible = False


class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем атрибут edible

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов и выполнение методов
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True
print(a2.fed)    # False

a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин

print(a1.alive)  # False
print(a2.fed)    # True