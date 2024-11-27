'''
Mohammed Nagla's Repository link - https://github.com/mohamed19874/Mohamed-nagla
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''

class Polygon:
    
    '''Creating the class strucutre for any and all 
    Polygons with the the initialized private variables
    of name and sides'''
    
    __slots__ = ['__name', '__sides']   #Used to create private variables

    def __init__(self, name, sides):
        """ initializing the attributes """
        self.__name = name    # name of polygon
        self.__sides = sides  # list of floats

    def get_name(self): #The getter (accessor) method for the polygon name
        return self.__name
    
    def set_name(self, newName): #The setter (mutator) method for the polygon name 
        self.__name = newName

    def get_sides(self): #The getter (accessor) method for the polygon sides
        return self.__sides
    
    def set_sides(self, newSides): #The setter (mutator) method for the polygon sides
        self.__sides = newSides

    def __eq__(self, polygonTwo): #The equality method to check the equality of two Polygon objects
        if type(self) == type(polygonTwo):  #First checks if the two objects are classes
            return self.__name == polygonTwo.__name and self.__sides == polygonTwo.__sides  #Then checks equality of the attributes of the class
        else:
            return False
        
    def __ne__(self, polygonTwo):   #The inequality method to check the equality of two Polygon objects
        return not self.__eq__(polygonTwo) #Using the __eq__ method and returning the opposite for efficiency
    
    def __str__(self): #defining the user-friendly representation of the polygon
        return f"{self.__name} with sides: {self.__sides}"
    
    def calculate_circumference(self): 

        '''A function designed to calculate the perimeter/circumference
         of the created polygon and return the perimeter/circumference'''

        circ = 0

        for side in self.__sides:
            circ += side

        return circ

def main():

    '''The main function to display the 
    functionality of the created class'''

    '''User input version of the code'''
    # Triangle = Polygon('Triangle', [(int(input("Enter a list of 3 sides for a triangle: ")))]) 
    # Square = Polygon('Square', [(int(input("Enter length of one side for a square: ")))]*4)
    # Hexagon = Polygon('Hexagon', [(int(input("Enter a list of 6 sides for a hexagon: ")))])

    '''Hard coded values version of the code'''
    Triangle = Polygon('Triangle', [13,12,5]) 
    Square = Polygon('Square', [4,4,4,4])
    Hexagon = Polygon('Hexagon', [2,4,2,5,6,3])
    
    print(Triangle) #Printing the details of the triangle and its calculated circumference     
    print(f'The circumference is: {Triangle.calculate_circumference()}')

    print(Square)   #Printing the details of the square and its calculated circumference
    print(f'The circumference is: {Square.calculate_circumference()}')
    
    print(Hexagon)  #Printing the details of the hexagon and its calculated circumference
    print(f'The circumference is: {Hexagon.calculate_circumference()}')    

if __name__ == '__main__':
    main()