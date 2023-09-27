from ShapeCalculator.Circle import Circle
import unittest


class TestShapeCircleCalculator(unittest.TestCase):
    def test_circle_area(self):
        calculator = Circle(5.0)
        self.assertAlmostEqual(calculator.get_area(), 78.54, places=2)

    def test_incorrect_radius(self):
        with self.assertRaises(ValueError):
            calculator = Circle(-1)


if __name__ == "__main__":
    unittest.main()
