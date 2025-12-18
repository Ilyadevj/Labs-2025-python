from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)
