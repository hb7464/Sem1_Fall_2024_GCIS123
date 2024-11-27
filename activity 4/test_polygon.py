import pytest
from polygon import Polygon
   
def test_Polygon_initialization():
    polygon1 = Polygon("Triangle", [5,5,5])
    assert polygon1.get_name() == "Triangle"
    assert polygon1.get_sides() == [5,5,5]
    
    polygon1.set_name("Pentagon")
    polygon1.set_sides([3,3,3,3,3])
    
    assert polygon1.get_name() == "Pentagon"
    assert polygon1.get_sides() == [3,3,3,3,3]

def test_polygon_equality():
    polygon1 = Polygon("Triangle", [9,9,9])
    polygon2 = Polygon("Triangle", [9,9,9])

    assert polygon1 == polygon2

def test_polygon_inequality():
    polygon1 = Polygon("Triangle", [7,7,7])
    polygon2 = Polygon("Pentagon", [7,7,7])

    assert polygon1 != polygon2

def test_polygon_str():
    Test_poly = Polygon('Square', [4,4,4,4])
    assert str(Test_poly) == 'Square with sides: [4, 4, 4, 4]'

def test_calculate_circumference():
    Test_poly = Polygon('Square', [4,4,4,4])
    assert pytest.approx(Test_poly.calculate_circumference()) == 16
