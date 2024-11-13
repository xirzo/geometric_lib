import unittest
from square import area, perimeter


class SquareTests(unittest.TestCase):
    def test_area_positive(self):
        side = 10
        expected_area = 100

        result = area(side)

        self.assertEqual(result, expected_area)

    def test_area_zero(self):
        side = 0

        expected_area = 0
        result = area(side)

        self.assertEqual(result, expected_area)

    def test_perimeter_positive(self):
        side = 10
        expected_perimeter = 40

        result = perimeter(side)

        self.assertEqual(result, expected_perimeter)

    def test_perimeter_zero(self):
        side = 0
        expected_perimeter = 0

        result = perimeter(side)

        self.assertEqual(result, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
