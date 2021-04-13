import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
colors = ("red", "blue", "yellow", "green", "white", "orange")

def draw_square(x, y, width, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)

    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

def draw_rubics_cube(x, y):
    size = 60
    width = size/3
    xpos = x
    ypos = y

    for row in range(3):
        ypos = y + row * width
        for col in range(3):
            color = colors[random.randint(0,len(colors)-1)]
            xpos = x + col * width
            draw_square(xpos, ypos, width, color)


turtle.onscreenclick(draw_rubics_cube)

turtle.done()