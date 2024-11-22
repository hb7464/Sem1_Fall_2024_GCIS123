class Graph:

    __slots__ = ['__xcoor','__ycoor']

    def __init__(self,xcoor,ycoor) -> None:
        self.__xcoor = xcoor
        self.__ycoor = ycoor

    def GetXcoor(self):
        return self.__xcoor
    
    def GetYcoor(self):
        return self.__ycoor
    
    def set_Xcoor(self,xcoor):
        self.__xcoor = xcoor

    def __str__(self):
        return f'X coordinate is: {self.GetXcoor()}\nY coordinate is: {self.GetYcoor()}'
    
a = Graph(10,5)
print(a)
print(repr(a))