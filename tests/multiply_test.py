"""Testing Multiplication Method"""
from calc.calculations.multiply import Multiplication

def test_calculation_multiplication():
    """Testing if the calculator has a static method for multiplication"""
    #Arrange
    my_nums = (2.0,3.0,0.5,1,0.5)
    #Act
    multiplication = Multiplication(my_nums)
    #Assert
    assert multiplication.get_result() == 1.5
