class Polygon_Test:
    
    __slots__ = ['__name', '__sides']

    def __init__(self, name, sides):
        self.__name = name
        self.__sides = sides

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_sides(self):
        return self.__sides
        
    def set_sides(self,sides):
        self.__sides = sides

    def __eq__(self,other):
        return self.__name == other.__name and self.__sides == other.__sides
    
    def __ne__(self,other):
        return self.__name != other.__name or self.__sides != other.__sides
    
    def __str__(self):
        return f"{self.__name} with sides: {self.__sides}"
    
    def calculate_circumference(self):
        circ = 0

        for side in self.__sides:
            circ += side

        return circ
    
def test_Polygon_initialization():
    Test_poly = Polygon_Test('triangle',[3,3,3])

def test_get_name():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    Test_poly.get_name()

def test_set_name():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    Test_poly.set_name('Rectangle')

def test_get_sides():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    Test_poly.get_sides()

def test_set_sides():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    Test_poly.set_sides([2,5,2,5])

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
    print(Test_poly)

def test_calculate_circumference():
    Test_poly = Polygon_Test('Square', [4,4,4,4])
    Test_poly.calculate_circumference()
