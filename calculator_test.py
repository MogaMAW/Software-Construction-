import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def __init__(self):
        """Initializes the calculator object."""
        pass

    def test_addition(self):#Adding two numbers.
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtraction(self): #Subtracting two numbers.
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiplication(self): #Multiplying two numbers.
        calc = Calculator()
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_division(self):
        calc = Calculator()
        self.assertEqual(calc.divide(6, 3), 2)

    def test_division_by_zero(self): #Raising ValueError if number2 is zero.
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()