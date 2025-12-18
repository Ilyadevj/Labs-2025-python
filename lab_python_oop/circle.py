import math
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Circle(GeometricFigure):
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{} радиус {}, цвет {}, площадь {:.2f}".format(
            self.name,
            self.radius,
            self.color.color,
            self.area()
        )
