import turtle as t

'''A program designed to create a 
cake on a table with user input'''

def table_leg():

    '''A function designed to create 
    the leg piece of a table'''
    
    t.down()
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(10)
    t.fillcolor('gray')
    t.end_fill()
    t.up()

def table():

    '''function to create the 2d 
    table with 4 legs'''

#This portion of code is to create the table top

    t.begin_fill()
    t.up()
    t.goto(-100,0)
    t.down()
    t.forward(200)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(10)
    t.fillcolor('white')
    t.end_fill()
    
#This is the portion of code dedicated to creating the legs of the table

    t.up()
    t.goto(-90,-10)
    t.right(180)
    table_leg()
    t.goto(-40,-10)
    t.left(90)
    table_leg()
    t.goto(30,-10)
    t.left(90)
    table_leg()
    t.goto(80,-10)
    t.left(90)
    table_leg()

def layer(height,width,col):
   
    '''This function is designed to 
    create each layer of the cake
    and takes 3 arguments, height of the layer, width of the layer and colour of the layer'''
    
    half = width//2
    t.up()
    t.begin_fill()
    t.down()
    t.forward(half)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(half)
    t.fillcolor(col)
    t.end_fill()
    t.up()

def deco():
    t.down()
    t.begin_fill()
    t.left(90)
    t.circle(5,180)
    t.left(180)
    t.circle(5,180)
    t.left(180)
    t.circle(5,180)
    t.left(180)
    t.circle(5,180)
    t.left(180)
    t.circle(5,180)
    t.left(180)
    t.circle(5,180)
    t.fillcolor('white')
    t.end_fill()
    print()

def cake_details():
    heig = float(input("Enter height of the layer: "))
    col = input("Enter a colour for the cake layer: ")
    return heig, col

def cake():
    stk = 0
    b = float(input("Enter the width of the cake (Has to be below 200px): "))
    a,c = cake_details()
    t.goto(0,stk)
    stk += a
    layer(a,b,c)
    a,c = cake_details()
    t.goto(0,stk)
    stk += a
    layer(a,b,c)
    a,c = cake_details()
    t.goto(0,stk)
    stk += a
    layer(a,b,c)
    t.goto(-b//2,stk)

def main():
    t.speed(100)
    t.bgcolor('sky blue')
    table()
    cake()
    deco()

    input()

main()