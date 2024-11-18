
'''Create a class, setup class level varialble values for 3 variables
first
second
third
all as zero

Create a constructor, pass on the values from atleast 3 instances and then call for
addition
subtraction
multiplication
and perform the operations'''

class calc:

    num1 = 0
    num2 = 0
    num3 = 0

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


    def disp(self):
        print(f'First Number: {self.num1}\Second Number: {self.num2}\nThird Number: {self.num3}')

    def add(self):
        self.addresult = self.num1 + self.num2
        print(self.addresult)

    def subtract(self):
        self.subresult = self.num1 - self.num2
        print(self.subresult)

    def multiply(self):
        self.multresult = self.num1 * self.num2
        print(self.multresult)

def main():

    inst1 = calc(10,20)
    inst1.add()
    print(inst1.num1,inst1.num2)
    print(calc.num1)
    inst2 = calc(3,2)
    inst2.subtract()
    inst3 = calc(71,1)    
    inst3.multiply()

if __name__ == '__main__':
    main()