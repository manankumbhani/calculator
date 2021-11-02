"""Testing the Calculator"""
from main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add(1)
    assert calc.result == 1

def test_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract(1)
    assert calc.get_result() == -1
def test_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    calc.multiply(1,2)
    assert calc.result == 2

def test1_divide():
    """ tests division of two numbers"""
    calc = Calculator()
    calc.divide(2, 1)
    assert calc.result == 2

def test2_divide():
    """ tests division of two numbers"""
    calc = Calculator()
    calc.divide(2,1)
    assert calc.result == 2, ZeroDivisionError
