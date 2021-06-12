#Python 3.9 Kalkulator Test

import unittest

from KALKULATOR import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc("+", 7, 3)
        self.assertEqual(10, result)
    def test_subtract(self):
        result = calc("-", 7, 3)
        self.assertEqual(4, result)
    def test_multiplay(self):
        result = calc("*", 5, 6)
        self.assertEqual(30, result)
    def test_divide(self):
        for x, y, result in [(6, 3, 2), (1, 2, 0.5), (-10, -5, 2)]:
            calculated_result = calc("/", x, y)
            self.assertEqual(result, calculated_result)
    def test_divide_with_y_as_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc("/", 1, 0)

if __name__ == '__main__':
    unittest.main()
