"""This is the multiply calculation that inherits the value A and value B from the calc class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """Multiplication class to get the result from Calculation class"""

    def get_result(self):
        """Defining get_result method"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
