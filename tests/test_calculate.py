import unittest
from calculate import calc


class CalculateTests(unittest.TestCase):

    def test_calc_circle_area_valid(self):
        fig = 'circle'
        func = 'area'
        size = [5]
        expected_result = 78.53981633974483

        result = calc(fig, func, size)

        self.assertAlmostEqual(result, expected_result, places=5)

    def test_calc_square_perimeter_valid(self):
        fig = 'square'
        func = 'perimeter'
        size = [5]
        expected_result = 20

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_triangle_area_valid(self):
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]
        expected_result = 6.0

        result = calc(fig, func, size)

        self.assertAlmostEqual(result, expected_result, places=5)

    def test_calc_invalid_figure(self):
        fig = 'wrong_figure'
        func = 'area'
        size = [5]

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertIn("Invalid figure", str(context.exception))

    def test_calc_invalid_function(self):
        fig = 'circle'
        func = 'wrong_function'
        size = [5]

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertIn("Invalid function", str(context.exception))

    def test_calc_invalid_size_attributes(self):
        fig = 'square'
        func = 'area'
        size = [5, 5]

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertIn("Invalid number of size attributes", str(context.exception))

    def test_calc_triangle_invalid_sides(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [1, 2, 10]

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertIn("Invalid triangle sides", str(context.exception))

    def test_calc_triangle_negative_sides(self):
        fig = 'triangle'
        func = 'area'
        size = [-3, 14, 5]

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertIn("Sides must be positive", str(context.exception))

    def test_calc_error_calculating(self):
        fig = 'circle'
        func = 'area'
        size = ['invalid']

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertIn("Error calculating", str(context.exception))


if __name__ == '__main__':
    unittest.main()
