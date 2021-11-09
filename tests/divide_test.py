"""Testing Division"""
import pytest
from calc.calculations.divide import Division

def test_calculation_division():
    """Testing that our calculator has a static method for multiplication"""
    #Arrange
    mynumbers = (2.0,2.0,2,0.5)
    #Act
    division = Division(mynumbers)
    #Assert
    assert division.get_result() == 0.25

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    mynumbers = (1.0, 0.0)
    # Act
    division = Division(mynumbers)
    # Assert
    with pytest.raises(ZeroDivisionError):
        result = division.get_result()
        assert result is True
