def prompt_print():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a,"+",b,"=",a+b)
    print(a,"-",b,"=",a-b)
    print(a,"x",b,"=",a*b)
    print(a,"/",b,"=",a/b)

def variables_prac():
    ageinmonths = int(input("How old are you? \n")) *12
    numofdaysinyear = 365 
    nameoffirstpet = input("Enter the name of your first pet: ")
    first5digitsofpi = 3.1415
    print(ageinmonths)
    print(numofdaysinyear)
    print(nameoffirstpet)
    print(first5digitsofpi)

variables_prac()