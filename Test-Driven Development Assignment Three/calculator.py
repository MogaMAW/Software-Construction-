class Calculator:
    """The calculator class contains methods for basic arithmetic operations."""
    def add(self, number1 , number2 ):
        return number1  + number2 

    def subtract(self, number1 , number2 ):
        return number1  - number2 

    def multiply(self, number1 , number2 ):
        return number1  * number2 

    def divide(self, number1 , number2 ):
        if number2  == 0:
            raise ValueError("Cannot divide by zero.")
        return number1 / number2 
