"""This is the subtract calculation that inherits the value A and value B from the calc class"""
from calc.calculation import Calculation


class Subtraction(Calculation):  # pylint: disable=too-few-public-methods
    """Subtraction class to get the result from Calculation class"""

    def get_result(self):
        """defining get_result method"""
        return self.value_a - self.value_b
