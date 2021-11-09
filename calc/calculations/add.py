"""This is the addition calculation that inherits the value A and value B from the calc class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):  # pylint: disable=too-few-public-methods
    """Addition class to get the result from parent Calculation class"""

    def get_result(self):
        """Defining get_result method"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
