import turtle as t

def intialization():
    global Pixel_Size 
    global ROWS 
    global COLUMNS
    Pixel_Size = 30
    ROWS = 20
    COLUMNS = 20
    t.speed(0)
    t.up()
    t.goto(-300,300)
    t.pencolor('black')
    t.fillcolor('white')

def box():
    t.begin_fill()
    t.down()
    c=0
    while c<4:
        t.right(90)
        t.forward(Pixel_Size)
        c+=1
    t.end_fill()
    t.up()
    t.forward(Pixel_Size)

def main():
    intialization()
    c=0
    while c< COLUMNS:
        box()
    input()

main()