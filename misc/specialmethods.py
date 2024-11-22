class Car:
    def __init__(self, vin, model, make):
        self.__vin = vin
        self.__model = model
        self.__make = make

    def __str__(self):
        return f"{self.__make} {self.__model} {self.__vin}"

    def __eq__(self,other):
        return self.__vin == other.__vin

    def __ne__(self,other):
        return self.__vin != other.__vin

    def __lt__(self,other):
        return self.__vin < other.__vin

    def __gt__(self,other):
        return self.__vin > other.__vin

    def __le__(self,other):
        return self.__vin <= other.__vin

    def __ge__(self,other):
        return self.__vin >= other.__vin

car1 = Car('123','corolla','toyota')
car2 = Car('456','altima','nissan')

print(car1)
print(car1 == car2)
print(car1 > car2)
print(car1 < car2)
print(car1)
print(car2)

class Car:
    def __init__(self, vin, model, make):
        self.__vin = vin
        self.__model = model
        self.__make = make

    def __str__(self):
        return f"{self.__make} {self.__model} {self.__vin}"

    def __hash__(self):
        return hash(self.__vin) * hash(self.__make) * hash(self.__model)

car1 = Car('123','corolla','toyota')
car2 = Car('456','altima','nissan')
print(f'Hash code for car1: {hash(car1)}')
print(f'Hash code for car2: {hash(car2)}')