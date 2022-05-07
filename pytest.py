import math
import pytest

# LOGIC TO BE TESTED CREATED
class Guvi:

    def odd_even(self, number):
        if(number%2==0):
            return "EVEN"
        else:
            return "ODD"

    def NameUpper(self, data):
        return data.upper()

    def NameLower(self, data):
        return data.lower()
    
    def SquareRoot(self, number):
        return math.sqrt(number)
    
    def NumberSquare(self, number):
        return number*number

# PYTEST FUNCTION WITH APPROPRIATE MARKERS & PARAMETERS CREATED

@pytest.mark.first
@pytest.mark.parametrize("input,output",[(2,4), (3,9), (10, 1000), (4,16)])
def test_first(input,output):
    assert Guvi().NumberSquare(input) == output


@pytest.mark.second 
@pytest.mark.parametrize("input,output", [(1,'ODD'),(2,'EVEN'),(3,'ODD'),(4,'EVEN')])
def test_second(input,output):
  
    assert Guvi().odd_even(input) == output
