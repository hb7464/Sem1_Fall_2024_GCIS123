class Bicycle:
    
    __slots__ = ['__color','__gears']
    
    def __init__(self,color,gears):
        self.__color = color
        self.__gears = gears

    def get_gears(self):
        return self.__gears
    
    def set_color(self,color):
        self.__color = color
        return self.__color
    
    def get_color(self):
        return self.__color

def main():
    bike = Bicycle('red',500)
    print(bike.get_gears())
    print(bike.get_color())
    print(bike.set_color('pink'))

if __name__ == '__main__':
    main()