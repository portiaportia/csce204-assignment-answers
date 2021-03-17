import turtle
import random

turtle.setup(1000,400)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
style = ("Arial", 18, "bold")

firstNames = []
lastNames = []
genders = []
phoneNumbers = []
index = 0

pen.up()
pen.setpos(-turtle.window_width()/2 + 10, turtle.window_height()/2 - 40)
pen.down()
pen.write("My Contact List", font = style)

numContacts = int(turtle.numinput("Contacts", "How many contacts do you have?:", 2, 0, 10))
style = ("Arial", 14 - numContacts, "bold")

for i in range(numContacts): 
    firstNames.append(turtle.textinput(f"Creating Contact {i+1}", "First Name:"))
    lastNames.append(turtle.textinput(f"Creating Contact {i+1}", "Last Name:"))
    genders.append(turtle.textinput(f"Creating Contact {i+1}", "Gender (Male or Female):"))
    phoneNumbers.append(turtle.textinput(f"Creating Contact {i+1}", "Phone Number:"))

padding = 10
width = turtle.window_width()/numContacts - padding * 2
manWidth = width / 5

if manWidth > 50:
    manWidth = 50

yPos = turtle.window_height()/4
pen.up()
pen.setx(-turtle.window_width()/2 + padding)

for i in range(numContacts):
    pen.color("black")
    pen.up()
    pen.sety(yPos)
    pen.down()
    pen.write(firstNames[i] + " " + lastNames[i], font = style)
    pen.up()
    pen.sety(yPos-20)
    pen.down()
    pen.write(phoneNumbers[i], font = style)
    pen.up()

    if(genders[i].strip().lower() == "female"):
        pen.color("pink")
    elif(genders[i].strip().lower() == "male"):
        pen.color("blue")
    
    # draw stick figure
    pen.sety(yPos-60 - manWidth)
    pen.forward(manWidth/2)
    pen.down()
    pen.circle(manWidth/2)
    #body
    pen.setheading(-90)
    pen.forward(manWidth)
    pen.up()
    #arms
    pen.setx(-turtle.window_width()/2 + padding + i* (width + padding))
    pen.sety(yPos-60 - manWidth - manWidth/2)
    pen.setheading(0)
    pen.down()
    pen.forward(manWidth)
    #left leg
    pen.up()
    pen.setx(-turtle.window_width()/2 + padding + i* (width + padding)+ manWidth/2)
    pen.sety(yPos-60 - manWidth - manWidth)
    pen.setheading(-120)
    pen.down()
    pen.forward(manWidth)
    #right leg
    pen.up()
    pen.setx(-turtle.window_width()/2 + padding + i* (width + padding)+ manWidth/2)
    pen.sety(yPos-60 - manWidth - manWidth)
    pen.setheading(-60)
    pen.down()
    pen.forward(manWidth)

    if(genders[i].strip().lower() == "female"):
        #dress bottom
        pen.up()
        pen.setheading(-180)
        pen.down()
        pen.forward(manWidth)

    pen.up()
    pen.setx(-turtle.window_width()/2 + padding + (i+1)* (width + padding))
    pen.setheading(0)

turtle.done()