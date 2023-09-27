import math
from ShapeCalculator.Interface.Figure import Figure


class Triangle(Figure):

    def __init__(self, side1: float, side2: float, side3: float):
        self._correct_args(side1, side2, side3)
        self.__is_triangle(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __is_triangle(self, side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        if not sides[0] + sides[1] > sides[2]:
            raise ValueError('A triangle with these sides does not exist')

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2

        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
