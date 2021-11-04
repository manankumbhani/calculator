""" This is the calculator function"""
from calc.add import Addition
from calc.subtract import Subtraction
from calc.multiply import Multiplication
from calc.divide import Division


class Calculator:
    """This is Calculator class"""

    history = []

    @staticmethod
    def get_history():
        """gets history"""
        get_history = Calculator.history
        return get_history

    @staticmethod
    def get_last_history_calculation():
        """gets last calculation from history"""
        return Calculator.history[-1]

    @staticmethod
    def get_first_history_calculation():
        """gets first calculation from history"""
        return Calculator.history[0]

    @staticmethod
    def get_last_history_calculation_result():
        """gets the result of last calculation from history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def clear_history():
        """clear the history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """count's the history"""
        return len(Calculator.history)

    @staticmethod
    def add_numbers(value_a, value_b):
        """ returns the sum of two numbers"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ returns the difference of the two numbers"""
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ returns the product of two numbers"""
        multiplication = Multiplication(value_a, value_b)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ returns the division of two numbers"""
        division = Division(value_a, value_b)
        Calculator.history.append(division)
        return division.get_result()
