import unittest
from ShapeCalculator.shapecalculator import ShapeCalculator
from ShapeCalculator.Triangle import Triangle


class TestShapeTriangleCalculator(unittest.TestCase):

    def test_triangle_area(self):
        calculator = Triangle(3.0, 4.0, 5.0)
        self.assertAlmostEqual(calculator.get_area(), 6.0, places=2)

    def test_is_right_triangle(self):
        right_triangle = Triangle(3.0, 4.0, 5.0)
        not_right_triangle = Triangle(2.0, 3.0, 4.0)
        self.assertTrue(right_triangle.is_right())
        self.assertFalse(not_right_triangle.is_right())

    def test_incorrect_sides(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(1.0, 14.0, 0.0)

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(-1.0, 14.0, 0.0)


if __name__ == "__main__":
    unittest.main()
