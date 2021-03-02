import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2) 
pen.speed(.5)
pen.color("black")
pen.hideturtle()

houseSize = 150

pen.up()
pen.setpos(-houseSize/4,-houseSize/2)
pen.down()
pen.fillcolor("orange")

#drawing house base
pen.begin_fill()
for i in range(4):
    pen.forward(houseSize/2)
    pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-houseSize * 1/3,0)
pen.down()
pen.fillcolor("purple")

#draw a triangle
pen.begin_fill()
for i in range(3):
    pen.forward(houseSize * 2/3)
    pen.left(120)
pen.end_fill()

# draw a star
starSize = houseSize / 4

pen.up()
pen.setpos(-200,200)
pen.down()
pen.color("yellow")
rays = 20

for i in range(rays):
    pen.up()
    pen.setpos(-200,200)
    pen.down()
    pen.forward(starSize)
    pen.left(360/rays)

#draw a tree
pen.up()
pen.setpos(houseSize /2,-houseSize/2)
pen.down()
pen.color("brown")
pen.fillcolor("brown")
treeSize = houseSize/8

pen.begin_fill()
for i in range(4):
    pen.forward(treeSize)
    pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(houseSize /2 + treeSize/2,-houseSize/2 + treeSize)
pen.down()
pen.color("green")
pen.fillcolor("green")
pen.begin_fill()
pen.circle(treeSize)
pen.end_fill()

turtle.done()