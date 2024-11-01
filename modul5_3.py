class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return True

    def add(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.add(value)

    def __radd__(self, value):
        return self.add(value)

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other.number_of_floors
        return FNotImplemented

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other.number_of_floors
        return True

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other.number_of_floors
        return False


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20


print(h1 == h2)  # False
h1.add(10)
print(h1)  # True
print(h1 == h2)
print(h1)  # True
h2.add(10)
print(h2)
print(h1 > h2)
print(h1 >= h2)  # False
print(h1 < h2)   # True
print(h1 <= h2)  # True
print(h1 != h2)  # True

