import turtle

turtle.setup(500,500)
turtle.bgcolor("skyblue")

pen = turtle.Turtle()

pen.pensize(5)
pen.speed(.5)
pen.fillcolor("brown")

# draw left arm
pen.penup()
pen.setpos(-50,100)
pen.begin_fill()
pen.pendown()
pen.setheading(180)
pen.forward(50)
pen.setheading(-90)
pen.forward(30)
pen.setheading(0)
pen.forward(50)
pen.setheading(90)
pen.forward(30)
pen.setheading(0)
pen.end_fill()

# draw right arm
pen.penup()
pen.setpos(50,100)
pen.begin_fill()
pen.pendown()
pen.setheading(0)
pen.forward(50)
pen.setheading(-90)
pen.forward(30)
pen.setheading(180)
pen.forward(50)
pen.setheading(90)
pen.forward(30)
pen.setheading(0)
pen.end_fill()

# draw body
pen.penup()
pen.setpos(0,-20)
pen.begin_fill()
pen.pendown()
pen.circle(70)
pen.end_fill()

# draw left ear
pen.penup()
pen.setpos(-28,190)
pen.begin_fill()
pen.pendown()
pen.circle(15)
pen.end_fill()

# draw right ear
pen.penup()
pen.setpos(28,190)
pen.begin_fill()
pen.pendown()
pen.circle(15)
pen.end_fill()

# draw head
pen.penup()
pen.setpos(0,100)
pen.begin_fill()
pen.pendown()
pen.circle(50)
pen.end_fill()

# draw left eye
pen.fillcolor("black")
pen.penup()
pen.setpos(-17,150)
pen.begin_fill()
pen.pendown()
pen.circle(10)
pen.end_fill()

# draw right eye
pen.fillcolor("black")
pen.penup()
pen.setpos(17,150)
pen.begin_fill()
pen.pendown()
pen.circle(10)
pen.end_fill()

# draw left foot
pen.fillcolor("brown")
pen.penup()
pen.setpos(-40,-40)
pen.begin_fill()
pen.pendown()
pen.circle(25)
pen.end_fill()

# draw right foot
pen.penup()
pen.setpos(40,-40)
pen.begin_fill()
pen.pendown()
pen.circle(25)
pen.end_fill()

turtle.done()