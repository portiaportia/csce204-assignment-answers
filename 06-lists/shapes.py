import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

numShapes = int(turtle.numinput("Shapes", "Enter Number of Shapes:", 5, 1, 10))
shapes = []
shapeHeight = (turtle.window_width()/2)/numShapes
padding = shapeHeight/4

for i in range(numShapes):
    shape = turtle.textinput("Shapes", f"Enter shape (circle, square, triangle, or star):")
    shapes.append(shape)

pen.up()
pen.setpos(-(shapeHeight + padding)*numShapes/2 - shapeHeight/2, 0)
pen.down()

for i in range(numShapes):
    forwardAmount = shapeHeight + padding
    if shapes[i] == "circle":
        pen.up()
        pen.forward(shapeHeight/2)
        pen.down()
        pen.circle(shapeHeight/2)
        forwardAmount = shapeHeight/2 + padding
    elif shapes[i] == "square":
        for i in range(4):
            pen.forward(shapeHeight)
            pen.left(90)
    elif shapes[i] == "triangle":
        for i in range(3):
            pen.forward(shapeHeight)
            pen.left(120)
    elif shapes[i] == "star":
        pen.up()
        pen.sety(shapeHeight/4)
        pen.down()
        for i in range(3):
            pen.forward(shapeHeight)
            pen.left(120)
        pen.setheading(0)
        pen.up()
        pen.sety(shapeHeight*3/4)
        pen.down()
        for i in range(3):
            pen.forward(shapeHeight)
            pen.left(-120)
        pen.up()
        pen.sety(0)
        pen.down()
    else:
        pen.write("X")

    pen.up()
    pen.setheading(0)
    pen.forward(forwardAmount + padding)
    pen.down()

turtle.done()