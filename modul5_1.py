class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for floor in range(1, new_floor + 1):
            if floor <= self.number_of_floors and self.number_of_floors > 2: # Проверка на наличие этажей и чтобы в проекте h2 не выводились этажи 1 и 2
                    print(floor)
            else:
                print("Такого этажа не существует")
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)

