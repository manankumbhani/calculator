"""Testing Subtraction Method"""
from calc.calculations.subtract import Subtraction

def test_calculation_subtraction():
    """Testing if the calculator has a static method for subtraction"""
    #Arrange
    my_nums = (1.0,2.0,0.5,3)
    #Act
    subtraction = Subtraction(my_nums)
    #Assert
    assert subtraction.get_result() == -6.5
