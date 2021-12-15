"""Testing Addition method"""
from calc.calculations.add import Addition

def test_calculation_addition():
    """Testing if the calculator has a static method for addition"""
    #Arrange
    my_nums = (1.0,2.0,3,4.5)
    #Act
    addition = Addition(my_nums)
    #Assert
    assert addition.get_result() == 10.5
