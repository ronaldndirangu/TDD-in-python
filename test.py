import unittest
import calc


class test_calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)
        self.assertIsInstance(calc.add(2,3), int)

    def test_subtract(self):
        self.assertEqual(calc.subtract(6,2), 4)
        self.assertIsInstance(calc.subtract(6,2), int)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2,3), 6)
        self.assertIsInstance(calc.multiply(2,3), int)

    def test_divide(self):
        self.assertEqual(calc.divide(6,3), 2)
        self.assertIsInstance(calc.divide(6,3), int)

if __name__ == "__main__":
    unittest.main()
