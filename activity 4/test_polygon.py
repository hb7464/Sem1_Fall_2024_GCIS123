import pytest
from polygon import Polygon as Polygon_Test
   
def test_Polygon_initialization():
    Test_poly = Polygon_Test('triangle',[3,3,3])
    assert Test_poly.get_name() == 'triangle' and Test_poly.get_sides() == [3,3,3]

def test_get_name():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    assert Test_poly.get_name() == 'Square'

def test_set_name():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    Test_poly.set_name('Rectangle')
    assert Test_poly.get_name() == 'Rectangle'

def test_get_sides():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    assert Test_poly.get_sides() == [4,4,4,4]

def test_set_sides():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    Test_poly.set_sides([2,5,2,5])
    assert Test_poly.get_sides() == [2,5,2,5]

def test_equality():
    Poly1 = Polygon_Test('Square',[4,4,4,4])
    Poly2 = Polygon_Test('Square',[4,4,4,4])
    assert Poly1 == Poly2

def test_inequality():
    Poly1 = Polygon_Test('Square',[4,4,4,4])
    Poly2 = Polygon_Test('Triangle',[3,3,3])
    assert Poly1 != Poly2

def test_polygon_str():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    assert str(Test_poly) == 'Square with sides: [4, 4, 4, 4]'

def test_calculate_circumference():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    assert pytest.approx(Test_poly.calculate_circumference()) == 16
