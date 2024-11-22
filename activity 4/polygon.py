class Polygon:
    
    '''Creating the class strucutre for any and all 
    Polygons with the the initialized private variables
    of name and sides'''
    
    __slots__ = ['__name', '__sides']   #Used to create private variables

    def __init__(self, name, sides): #The initialization function with the name and list of sides
        self.__name = name
        self.__sides = sides

    def get_name(self): #The getter (accessor) function for the polygon's name
        return self.__name

    def set_name(self,name): #The setter (mutator) function for the polygon's name
        self.__name = name

    def get_sides(self): #The getter (accessor) function for the polygon's sides
        return self.__sides
        
    def set_sides(self,sides): #The setter (mutator) function for the polygon's sides
        self.__sides = sides

    def __eq__(self,other): #The equality checker function for 2 polygons
        return self.__name == other.__name and self.__sides == other.__sides
    
    def __ne__(self,other): #The inequality checker function for 2 polygons
        return self.__name != other.__name or self.__sides != other.__sides
    
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