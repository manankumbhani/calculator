"""Testing Division"""
from calc.calculations.divide import Division

def test_calculation_division():
    """Testing that our calculator has a static method for division"""
    #Arrange
    mynumbers = (2.0,2.0)
    #Act
    division = Division(mynumbers)
    #Assert
    assert division.get_result() == 1.0

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    mynumbers = (1.0, 0.0)

    try:
        division = Division(mynumbers)
        division.get_result()

    except ZeroDivisionError as message:
        print(message)
