import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(.5)
pen.pensize(2)
pen.hideturtle()

#draw head
faceRadius = 100
pen.up()
pen.setpos(0,-faceRadius)
pen.down()
pen.circle(faceRadius)

#draw left eye
eyeRadius = faceRadius/8
pen.fillcolor("black")
pen.up()
pen.setpos(-faceRadius/4,0)
pen.down()
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()

#draw right eye
eyeRadius = faceRadius/8
pen.fillcolor("black")
pen.up()
pen.setpos(faceRadius/4,0)
pen.down()
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()

grade = turtle.numinput("Grades", "Enter Grade")
if grade > 80:
    #draw smile
    smileRadius = faceRadius/2
    pen.fillcolor("black")
    pen.up()
    pen.setpos(-smileRadius*5/6,-faceRadius/3)
    pen.down()
    pen.setheading(-60)
    pen.circle(smileRadius, 120)
elif grade > 70:
    #draw smile
    flatSmile = faceRadius/2
    pen.fillcolor("black")
    pen.up()
    pen.setpos(-flatSmile/2,-faceRadius/2)
    pen.down()
    pen.setheading(0)
    pen.forward(flatSmile)
else:
    #draw frown
    smileRadius = faceRadius/2
    pen.fillcolor("black")
    pen.up()
    pen.setpos(-smileRadius*5/6,-faceRadius/2)
    pen.down()
    pen.setheading(60)
    pen.circle(-smileRadius,120)

turtle.done()