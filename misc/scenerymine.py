import turtle as t

'''A program designed to create a 
cake on a table with user input'''

def table_leg(hei,col):

    '''A function designed to create 
    the leg piece of a table'''
    
    t.down()
    t.begin_fill()
    t.forward(hei)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(hei)
    t.left(90)
    t.forward(10)
    t.fillcolor(col)
    t.end_fill()
    t.up()

def table(wid,col):

    '''function to create the 2d 
    table with 4 legs'''

#This portion of code is to create the table top

    strt = wid//2

    t.begin_fill()
    t.up()
    t.goto(-(strt),0)
    t.down()
    t.forward(wid)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(wid)
    t.right(90)
    t.forward(10)
    t.fillcolor(col)
    t.end_fill()
    
#This is the portion of code dedicated to creating the legs of the table
    
    l = float(input("Enter the length of table leg: "))
    c = input("Enter the colour of table legs: ")

    t.up()
    t.goto(-(strt-10),-10)
    t.right(180)
    table_leg(l,c)
    t.goto(-40,-10)
    t.left(90)
    table_leg(l,c)
    t.goto(30,-10)
    t.left(90)
    table_leg(l,c)
    t.goto((strt-20),-10)
    t.left(90)
    table_leg(l,c)

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

def deco(stk):
    t.goto(0,stk)
    t.down()
    t.begin_fill()
    t.left(90)
    t.circle(5,180)
    t.left(180)
    t.circle(5,180)
    t.left(180)
    t.circle(5,180)
    t.fillcolor('white')
    t.end_fill()
    
    t.goto(0,stk)
    t.begin_fill()
    t.left(180)
    t.circle(-5,180)
    t.left(180)
    t.circle(-5,180)
    t.left(180)
    t.circle(-5,180)
    t.end_fill()
    t.goto(0,stk)
    t.up()

def candle(stk):
    
    '''The function to create a candle 
    on top of the cake'''

    t.goto(-2.5,stk)
    t.down()
    t.begin_fill()
    t.forward(15)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(5)
    t.fillcolor('dark red')
    t.end_fill()
    t.up()
    t.goto(0,stk)
    t.right(90)
    t.forward(15)
    t.down()
    t.pencolor('yellow')
    t.forward(5)
    t.up()
    t.goto(100,100)

def cake_details():
    
    #function to take user input for each layer of the cake
    
    heig = float(input("Enter height of the layer: "))
    col = input("Enter a colour for the cake layer: ")
    return heig, col

def cake():
    
    '''The cake function is designed to make the 
    actual base cake with the neccesary layers'''
    
    stk = 0 #To move the pen to the right height after creating each layer so the layers don't overlap
    b = float(input("Enter the width of the cake (Has to be below 200px): "))
    
    #To check the cake will not be bigger than the table

    if b > 200:
    
        print("Cake is too big")
    
    else:
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

        print("Adding decorations")
        deco(stk)
        
        return stk

def main():
    t.speed(100)
    t.bgcolor('sky blue')
    
    wid = float(input("Enter how wide the table should be: "))
    col = input("Enter the colour of the table: ")
   
    print("Setting up the table")
    table(wid,col)
   
    print("Cake being prepapred")
    stk = cake()

    print("Adding a candle")
    candle(stk)

    print("Happy birthday!")
    input("Press enter to close out of the program")

main()