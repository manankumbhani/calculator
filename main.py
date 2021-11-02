""" This is the calculator function"""


class Calculator:
    """This is Calculator class"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add(self, val_a):
        """ Adds the value_a to result and store the value """
        self.result = self.result + val_a
        return self.result

    def subtract(self, val_a):
        """ Subtracts the Value_a from result and store the value """
        self.result = self.result - val_a
        return self.result

    def multiply(self, val_a, val_b):
        """ multiplying the value_a and value_b and store the value """
        self.result = val_a * val_b
        return self.result

    def divide(self, val_a, val_b):
        """ Dividing the value_a and value_b and store the value """
        self.result = val_a / val_b
        return self.result
