"""This is the subtract calculation that inherits the value A and value B from the calc class"""
from calc.calculations.calculation import Calculation

class Subtraction(Calculation):  # pylint: disable=too-few-public-methods
    """Subtraction class to get the result from Calculation class"""

    def get_result(self):
        """Defining get_result method"""
        diff_of_values = 0.0
        for value in self.values:
            diff_of_values = diff_of_values - value
        return diff_of_values
