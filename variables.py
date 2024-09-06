
"""Expressions can use input provided by the user as well as literal
values and variables in your program. Experiment by prompting the
user to enter values and then use those values in several different
expressions. Enter a number: 12
Enter another: 14
12 + 14 = 26
12 - 14 = -2
12 * 14 = 168
12 / 14 = 0.8571428571
● Add a new function called “prompt_and_print” to your “variables.py”
program and:
○ Prompt the user to enter two numeric values (one at a time).
○ Print the result of adding, subtracting, multiplying, and dividing the two numbers.
● Don’t forget to call your function.
● Run your program.
● Add a comment to the top of the function to describe what happens.
● Don’t forget to push your code to GitHub."""

def prompt_print():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a,"+",b,"=",a+b)
    print(a,"-",b,"=",a-b)
    print(a,"x",b,"=",a*b)
    print(a,"/",b,"=",a/b)

"""Using variables makes your code a lot more flexible and easier to
understand (assuming that they are named clearly). You will be
using lots of variables in your programs. Start practicing now.
● Start a new Python program, “variables.py”.
● Start a new function named “variable_practice” and:
○ Declare a variable with a descriptive name and initialize it with a value of an
appropriate type for each of the following:
■ Your age in months.
■ The number of days in a year.
■ The name of your first pet.
■ The first 5 digits of Pi.
○ Print all of your variable names and values.
● Don’t forget to call your function at the bottom of your program.
● Once you have verified that your program is working, push it to GitHub.
"""

def variables_prac():
    ageinmonths = 217
    numofdaysinyear = 365 
    nameoffirstpet = 'yguhj'
    first5digitsofpi = 3.1415
    print("Age in months: ",ageinmonths)
    print("Number of days in a year: ",numofdaysinyear)
    print("Name of first pet: ",nameoffirstpet)
    print("First 5 digits of Pi: ",first5digitsofpi)

"""Expressions allow your programs to compute or combine values
dynamically at runtime. These values may change from one run to
the next! Try initializing a few variables using expressions.
● Add a new function called “expressions_practice” to your
“variables.py” program and:
○ Declare and initialize a variable with a descriptive name for each of the following
expression types:
■ Literal
■ Addition
■ Exponent
■ Floor division
■ Mod
■ Use parentheses to perform addition and subtraction before multiplication
■ A mix of at least four different arithmetic operators
○ Print each of the variables.
● Don’t forget to call your function.
● Once you have verified that your program is working, push it to GitHub.
"""

def expressions_prac():
    Literal = 'str'
    Addition = 1+4
    Exponent = 3**7
    Floor_division = 12//5
    Mod = 279%3
    Pemdas = (24+2)*4
    mix = (26-2)*3/4
    print("Literal: ", Literal)
    print("Addition: ",Addition)
    print("Exponent: ", Exponent)
    print("Floor division: ", Floor_division)
    print("Mod: ",Mod)
    print("Pemdas: ",Pemdas)
    print("Mixed Operations: ", mix)
expressions_prac()