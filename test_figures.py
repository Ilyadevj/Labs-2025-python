import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
import math

class TestFigures(unittest.TestCase):

    def test_rectangle_area(self):
        r = Rectangle(2, 3, "blue")
        self.assertEqual(r.area(), 6)

    def test_square_area(self):
        s = Square(4, "red")
        self.assertEqual(s.area(), 16)

    def test_circle_area(self):
        c = Circle(1, "green")
        self.assertAlmostEqual(c.area(), math.pi, places=5)

if __name__ == "__main__":
    unittest.main()
