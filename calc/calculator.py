""" This is the calculator function"""
from calc.history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """ adds a list of numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplies a number with the result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ Divides a number from the result"""
        Calculations.add_division_calculation(tuple_values)
        return True
