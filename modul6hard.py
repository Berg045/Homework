import math

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.sides = list(sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.sides

    def __is_valid_color(self, r, g, b):
        for x in (r, g, b):
            if not (isinstance(x, int) and 0 <= x <= 255):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if not (isinstance(side, int) and side > 0):
                    return False
            return True
        return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides = list(new_sides)

    def len(self):
        return sum(self.sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 0:
            self.set_sides(1)

    def radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.radius() ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 0:
            self.set_sides(1, 1, 1)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(sides) > 0:
            self.sides = [sides[0]] * self.sides_count

    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())  # [15]
print(circle1.len())  # 15
print(cube1.get_volume()) 
print(circle1.get_sides()) 
print(len(circle1))  # 15
print(cube1.get_volume())
