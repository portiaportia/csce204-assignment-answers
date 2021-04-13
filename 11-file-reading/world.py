import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def getScene():
    sceneItems = []
    with open("assignments/10-file-reading/scene.txt") as file:
        for line in file:
            item = line.replace("\n", "").strip().lower()
            sceneItems.append(item)
        return sceneItems

def drawStar(x, width):
    pen.color("gold")
    drawTriangle(x,-width/4,width)
    drawUpsideDownTriangle(x,width/4,width)

def drawTree(x, width):
    pen.color("forest green")
    drawTriangle(x,-width/2,width)
    drawTriangle(x + width * .1,-width/8, width * .8)
    drawTriangle(x + width * .2,width/4,width * .6)

def drawTriangle(x,y,size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def drawUpsideDownTriangle(x,y,size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.right(120)
    pen.end_fill()

items = getScene()
numItems = len(items)
width = turtle.window_width()/numItems
padding = width/10
width = width - padding * 2
x = -turtle.window_width()/2

for item in items:
    if item == "star":
        drawStar(x + padding,width)
    elif item == "tree":
        drawTree(x + padding,width)
    x += width + padding * 2

turtle.done()