"""This is the divide calculation that inherits the value A and value B from the calc class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):  # pylint: disable=too-few-public-methods
    """Division class to get the result from Calculation class"""

    def get_result(self):
        """Defining get_result method"""
        result = self.values[0] / self.values[1]
        return result
