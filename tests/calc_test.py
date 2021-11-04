"""Testing the Calculator"""
import pprint

from calculator.main import Calculator


def test_calculator_add():
    """test the addition function"""
    assert Calculator.clear_history()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_last_history_calculation_result() == 6
    pprint.pprint(Calculator.history)


def test_clear_history():
    """Testing the clear history"""
    assert Calculator.clear_history()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history()
    assert Calculator.history_count() == 0


def test_count_history():
    """ testing the count of history"""
    assert Calculator.clear_history()
    assert Calculator.history_count() == 0
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.history_count() == 2


def test_get_last_calculation_result():
    """Testing the last calculation result """
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.get_last_history_calculation_result() == 5


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_numbers(1, 2) == -1


def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_divide():
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(2, 1) == 2


def test_get_first_calculation():
    """testing to see the first calculation in history"""
    assert Calculator.get_first_history_calculation() == Calculator.history[0]


def test_get_last_calculation_object():
    """testing to verify the last calculation in the history"""
    assert Calculator.get_last_history_calculation() == Calculator.history[-1]


def test_add_calculation_to_history_():
    """testing to check the addition of history"""
    assert Calculator.clear_history()
    old_count = Calculator.history_count()
    assert Calculator.add_numbers(1, 2) == 3
    new_count = Calculator.history_count()
    assert new_count == old_count + 1


def test_get_first_calculation_test():
    """test to get the first calculation"""
    assert Calculator.clear_history()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    calculation = Calculator.history[0].get_result()
    assert calculation == 3


def test_get_last_calculation():
    """test to get the last calculation"""
    assert Calculator.clear_history()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    calculation = Calculator.history[-1].get_result()
    assert calculation == 6


def test_get_history():
    """test the history of calculation"""
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    get_his = Calculator.get_history()
    assert get_his
