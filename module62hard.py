from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self,  color, *sides):
        self.__sides = []
        self.__color = [None, None, None]
        self.filled = False
        if isinstance(color, list | tuple) and len(color) == 3:
            self.set_color(color[0], color[1], color[2])
        if self.sides_count == len(sides) and self.__is_valid_sides(*sides):
            self.set_sides(*sides)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides.clear()
            for j in sides:
                self.__sides.append(j)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if not (isinstance(side, int) and side > 0):
                    return False
            return True
        else:
            return False

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_radius()

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__radius = self.get_radius()

    def get_radius(self):
        return self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.get_height()

    def set_sides(self, *sides):
        super().set_sides(*sides)
        if (self.get_sides()[0] + self.get_sides()[1] > self.get_sides()[2] and
                self.get_sides()[1] + self.get_sides()[2] > self.get_sides()[0] and
                self.get_sides()[2] + self.get_sides()[0] > self.get_sides()[1]):
            self.__height = self.get_height()
        else:
            self.set_sides(1, 1, 1)

    def get_height(self):
        p = self.__len__()/2
        return (2 * sqrt(p * (p - self.get_sides()[0]) *
                         (p - self.get_sides()[1]) *
                         (p - self.get_sides()[2]))) / self.get_sides()[0]

    def get_square(self):
        return (self.get_sides()[0] * self.get_height()) / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side_12 = sides * 12
        super().__init__(color, *side_12)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())


cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
print(circle1.get_sides())


print(len(circle1))


print(cube1.get_volume())
