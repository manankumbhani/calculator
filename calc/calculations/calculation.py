"""This is an abstract Calculation Class"""
class Calculation:  # pylint: disable=too-few-public-methods
    """Class docstring"""

    def __init__(self,values: tuple):
        """Method constructor"""
        self.values = Calculation.convert_args_to_list_float(values)
    @staticmethod
    def convert_args_to_list_float(values):
        """ Standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
