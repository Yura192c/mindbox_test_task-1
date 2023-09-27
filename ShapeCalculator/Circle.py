import math
from ShapeCalculator.Interface.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: float):
        self._correct_args(radius)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)
