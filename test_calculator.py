import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(0, 1), 1)

    def test_add_3(self):
        self.assertEqual(self.calc.add("a", 1), "Please enter only integer")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(0, 1), -1)

    def test_subtract_3(self):
        self.assertEqual(self.calc.subtract(1, 4), -3)

    def test_subtract_4(self):
        self.assertEqual(self.calc.subtract("A", 2), "Please enter only integer")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(0, 11), 0)

    def test_multiply_3(self):
        self.assertEqual(self.calc.multiply(-1,3), -3)

    def test_multiply_4(self):
        self.assertEqual(self.calc.multiply(-3,-3), 9)

    def test_multiply_5(self):
        self.assertEqual(self.calc.multiply(-4,0), 0)

    def test_multiply_6(self):
        self.assertEqual(self.calc.multiply(1,-3), -3)

    def test_multiply_7(self):
        self.assertEqual(self.calc.multiply("Hello", 3), "Please enter only integer")

    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2), 2)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(0, 2), 0)

    def test_divide_3(self):
        self.assertEqual(self.calc.divide(4,0), "Divided by zero")

    def test_divide_4(self):
        self.assertEqual(self.calc.divide(5,2), 2)

    def test_divide_5(self):
        self.assertEqual(self.calc.divide(5,"a"), "Please enter only integer")

    def test_divide_6(self):
        self.assertEqual(self.calc.divide(-2, 2), -1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(4,2), 0)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(5,2), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()