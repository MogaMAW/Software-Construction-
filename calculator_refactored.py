class Calculator_Refactored:
    """The calculator refactored class contains methods for basic arithmetic operations."""
    @staticmethod
    def add(number1, number2 ):
        return number1 + number2 

    @staticmethod
    def subtract(number1, number2):
        return number1 - number2

    @staticmethod
    def multiply(number1, number2):
        return number1 * number2

    @staticmethod
    def divide(number1, number2):
        if number2 == 0:
            raise ValueError("Cannot divide by zero.")
        return number1 / number2
