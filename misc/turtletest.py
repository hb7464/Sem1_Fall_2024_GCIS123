"""
Create a new Python module in a file named "turtle_stuff.py".
○ Don't forget to import turtle at the top of your program.
● Add a function called "test_drive" and use it to issue commands to your
turtle. Remember the turtle can:
○ Move forward some distance, e.g. turtle.forward(100)
○ Turn left or right some number of degrees, e.g. turtle.left(87)
○ Turn to face a specific angle, e.g. turtle.setheading(127)
○ Raise or lower the pen, i.e. turtle.up() & turtle.down()
○ Warp to a specific coordinate on the screen, e.g. turtle.goto(50, 50)
○ Return to the home position in the center, i.e. turtle.home()
○ Draw circles of a specified radius, e.g. turtle.circle(25)
● Don't forget to call your function from main!
● Run your program. What happens?
"""

from turtle import *
def test_drive():
    speed(1)
    forward(100)
    left(87)
    setheading(127)
    up()
    goto(50,50)
    down()
    home()
    circle(25)
    input()

def turtle_circle():
    circle(34.5)

def main():
    turtle_circle()

main()