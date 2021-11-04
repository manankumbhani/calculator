"""This is the multiply calculation that inherits the value A and value B from the calc class"""
from calc.calculation import Calculation


class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """Multiplication class to get the result from Calculation class"""

    def get_result(self):
        """defining get_result method"""
        return self.value_a * self.value_b
