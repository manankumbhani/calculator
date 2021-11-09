""" This is the calculator function"""
from calc.calculations.add import Addition
from calc.calculations.subtract import Subtraction
from calc.calculations.multiply import Multiplication
from calc.calculations.divide import Division
from calc.history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def add_numbers(*args):
        """ adds a list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """ multiplies a number with the result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def divide_numbers(*args):
        """ Divides a number from the result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
