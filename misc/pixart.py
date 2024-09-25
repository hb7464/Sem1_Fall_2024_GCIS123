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

def row():
    c=0
    while c < COLUMNS:
        box()
        c+=1
        
def main():
    t.Screen().setup(width=0.5, height=0.75, startx=None, starty=None)
    intialization()
    i = 0
    while i < ROWS:
        i+=1
        t.up()
        t.goto(-300,300-(i*Pixel_Size))
        row()
    input()

main()