import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(0, 1), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()