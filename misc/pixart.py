import turtle as t

Pixel_Size = 30
ycoor = Pixel_Size*10
xcoor = -Pixel_Size*10

def get_colour(n):

    '''A function designed to take 
    in a character and return a colour'''

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

    '''A function designed to draw a 
    pixel with the inputed color'''
    
    turta.setheading(0)
    turta.pencolor('black')
    turta.fillcolor(color_string)
    turta.begin_fill()
        
    for j in range(4):
        turta.forward(Pixel_Size)
        turta.left(90)

    turta.forward(Pixel_Size)
    turta.end_fill()

def draw_pixel(color_string_number, turta):
    
    '''A function that uses the draw_color_pixel function and get colour 
    function in tandem to draw a pixel of a user desired color'''

    color_string = get_colour(color_string_number)
    draw_color_pixel(color_string,turta)

def draw_line_from_string(color_string_line, turta):  

    '''A function that takes a string of characters and 
    draws a line using the draw_pixel function in a loop'''
    
    try:

        for i in color_string_line:    
            draw_pixel(i,turta)
    
    except:
    
        return False

def draw_shape_from_string(turta):

    '''A function designed that takes user input continuously
     and draws pixel of the associated colors to the string 
     until the user inputs an empty string or an invalid 
     character not associated with any color'''
    
    Row=0
    while True:
        
        turta.up()
        t.goto(xcoor,ycoor-(Row*Pixel_Size))
        turta.down()

        Row+=1
        color_string = input("Enter a color string: ")
        
        if color_string == '' or draw_line_from_string(color_string, turta) == False:
            break
        
def draw_grid(turta):

    '''A function that draws a grid with a 
    black and red checkerboard pattern using 
    the draw_line_from_string function'''

    turta.speed(0)
    turta.up()
    turta.goto(xcoor,ycoor)

    for i in range(20):
        
        turta.down()
        if i%2 == 0:
            draw_line_from_string('02020202020202020202',turta)
        else:    
            draw_line_from_string('20202020202020202020',turta)
            
        turta.up()
        t.goto(xcoor,ycoor-((i+1)*Pixel_Size))
    
def draw_shape_from_file(turta):
    
    '''A function designed to take a file path 
    from the user that contains characters that 
    correlate to colors as listed in the get_colour
    function and reads the file line by line feeding
    it into the draw_line_from_string function to 
    create a full image'''
    
    filepath = input("Enter a file path: ")
    with open(filepath) as file:
        
        Row=0
        
        for line in file:
            
            turta.goto(xcoor,ycoor-(Pixel_Size*Row))
            draw_line_from_string(line, turta)
            Row += 1
    
def main():
    t.tracer(False)
    t.speed(0)
    draw_shape_from_string(t)
    #draw_shape_from_file(t)
    input()

if __name__ == '__main__':
    main()