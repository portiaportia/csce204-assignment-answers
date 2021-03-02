import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

numLines = int(turtle.numinput("Pyramid", "Enter Height:", 5, 1, 10))
colors = []
triHeight = (turtle.window_width()/2)/numLines

for i in range(numLines):
    color = turtle.textinput("Pyramid", f"Enter color of row {i+1}:")
    colors.append(color)

pen.up()
pen.setpos(-triHeight*numLines/2, -triHeight*numLines/2)
pen.down()

for i in range(numLines + 1):
    for j in range(numLines - i):
        pen.fillcolor(colors[i])
        pen.color(colors[i])
        pen.begin_fill()
        for k in range(3):
            pen.forward(triHeight)
            pen.left(120)
        pen.end_fill()
        pen.setheading(0)
        pen.forward(triHeight)
    pen.setheading(90)
    pen.up()
    pen.forward(triHeight)
    pen.setheading(0)
    pen.forward(-triHeight * (numLines -i) + triHeight/2)
    pen.down()


turtle.done()