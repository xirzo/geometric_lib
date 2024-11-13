import unittest
import math
from triangle import area, perimeter


class TriangleTests(unittest.TestCase):
    def test_area_positive(self):
        x, y, z = 3, 4, 5
        expected_area = 6.0

        result = area(x, y, z)

        self.assertAlmostEqual(result, expected_area, places=5)

    def test_perimeter_positive(self):
        x, y, z = 1, 1, 1

        expected_perimeter = 3

        result = perimeter(x, y, z)

        self.assertEqual(result, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
