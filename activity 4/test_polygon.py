import pytest
import polygon
   
def test_Polygon_initialization():
    polygon1 = polygon.Polygon("Triangle", [5,5,5])
    assert polygon1.get_name() == "Triangle"
    assert polygon1.get_sides() == [5,5,5]

def test_get_name():
    polygon1 = polygon.Polygon("Pentagon", [5,5,5])
    assert polygon1.get_name() == "Pentagon"

def test_set_name():
    polygon1 = polygon.Polygon("Triangle", [5,5,5])
    polygon1.set_name("Pentagon")    
    assert polygon1.get_name() == "Pentagon"

def test_get_sides():
    polygon1 = polygon.Polygon("Triangle", [5,5,5])
    assert polygon1.get_sides() == [5,5,5]

def test_set_sides():
    polygon1 = polygon.Polygon("Triangle", [5,5,5])
    polygon1.set_sides([3,3,3,3,3])
    assert polygon1.get_sides() == [3,3,3,3,3]

def test_polygon_equality():
    polygon1 = polygon.Polygon("Triangle", [9,9,9])
    polygon2 = polygon.Polygon("Triangle", [9,9,9])

    assert polygon1 == polygon2

def test_polygon_inequality():
    polygon1 = polygon.Polygon("Triangle", [7,7,7])
    polygon2 = polygon.Polygon("Pentagon", [7,7,7])

    assert polygon1 != polygon2

def test_polygon_str():
    Test_poly = polygon.Polygon('Square', [4,4,4,4])
    assert str(Test_poly) == 'Square with sides: [4, 4, 4, 4]'

def test_calculate_circumference():
    Test_poly = polygon.Polygon('Square', [4,4,4,4])
    assert pytest.approx(Test_poly.calculate_circumference()) == 16
