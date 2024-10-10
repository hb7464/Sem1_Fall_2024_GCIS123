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

def get_colour(n):

    if n == '0':
        return 'black'
    elif n == '1':
        return 'white'
    elif n == '2':
        return 'red'
    elif n == '3':
        return 'yellow'
    elif n == '4':
        return 'orange'
    elif n == '5':
        return 'green'
    elif n == '6':
        return 'yellowgreen'
    elif n == '7':
        return 'sienna'
    elif n == '8':
        return 'tan'
    elif n == '9':
        return 'gray'
    elif n == 'A':
        return 'darkgray'

def draw_color_pixel(color_string, turta):

    turta.setheading(0)
    turta.pencolor('black')
    turta.fillcolor(color_string)
    turta.begin_fill()
        
    for j in range(4):
        turta.forward(20)
        turta.left(90)

    turta.forward(20)
    turta.end_fill()

def draw_pixel(color_string_number, turta):
    color_string = get_colour(color_string_number)
    draw_color_pixel(color_string,turta)

def draw_line_from_string(color_string_line, turta):    #Check if its fine that i slightly changed the values
    
    try:

        for i in color_string_line:     #Ask professor whether i should use try&except or can i use if i not in statement
            draw_pixel(i,turta)
    
    except:
    
        return False

def draw_shape_from_string(turta):
    
    while True:
        
        color_string = input("Enter a color string: ")
        
        if color_string == '' or draw_line_from_string(color_string, turta) == False:
            break
        
def draw_grid(turta):

    turta.speed(0)
    turta.up()
    turta.goto(-200,100)

    for i in range(20):
        
        turta.down()
        if i%2 == 0:
            draw_line_from_string('02020202020202020202',turta)
        else:    
            draw_line_from_string('20202020202020202020',turta)
            
        turta.up()
        t.goto(-200,100-((i+1)*20))
    
def draw_shape_from_file(turta):
    
    filepath = input("Enter a file path: ")
    with open(filepath) as file:
        
        Row=0
        
        for line in file:
        
            turta.goto(-200,200-(20*Row))
            draw_line_from_string(line, turta)
            Row += 1
    
def main():
    t.tracer(False)
    t.speed(0)
    draw_shape_from_file(t)
    input()

if __name__ == '__main__':
    main()