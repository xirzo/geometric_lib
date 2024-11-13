import unittest
from circle import area, perimeter


class CircleTests(unittest.TestCase):
    def test_area_positive(self):
        radius = 10

        expected_area = 314.15927

        result = area(radius)

        self.assertAlmostEqual(result, expected_area, places=5)

    def test_area_zero(self):
        radius = 0

        expected_area = 0

        result = area(radius)

        self.assertEqual(result, expected_area)

    def test_perimeter_positive(self):
        radius = 10

        expected_perimeter = 62.83185

        result = perimeter(radius)

        self.assertAlmostEqual(result, expected_perimeter, places=5)

    def test_perimeter_zero(self):
        radius = 0

        expected_perimeter = 0

        result = perimeter(radius)

        self.assertEqual(result, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
