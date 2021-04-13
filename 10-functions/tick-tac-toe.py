import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

osPlaying = True
playerSize = turtle.window_width()/5

def draw_grid():
    # left down line
    pen.up()
    pen.setpos(-turtle.window_width()/2 + turtle.window_width()/3, turtle.window_height()/2)
    pen.setheading(-90)
    pen.down()
    pen.forward(turtle.window_height())

    # right down line
    pen.up()
    pen.setpos(turtle.window_width()/2 - turtle.window_width()/3, turtle.window_height()/2)
    pen.setheading(-90)
    pen.down()
    pen.forward(turtle.window_height())

    # up right line
    pen.up()
    pen.setpos(-turtle.window_width()/2, turtle.window_height()/2 - turtle.window_height()/3)
    pen.setheading(0)
    pen.down()
    pen.forward(turtle.window_width())

    # down right line
    pen.up()
    pen.setpos(-turtle.window_width()/2, turtle.window_height()/2 - turtle.window_height()/3 * 2)
    pen.setheading(0)
    pen.down()
    pen.forward(turtle.window_width())

def draw_O(x,y):
    pen.penup()
    pen.setpos(x,y - playerSize/2)
    pen.down()
    pen.circle(playerSize/2)

def draw_X(x,y):
    pen.penup()
    pen.setpos(x-(playerSize/3),y + (playerSize/3))
    pen.down()
    pen.setheading(-45)
    pen.forward(playerSize)

    pen.penup()
    pen.setpos(x+(playerSize/3),y + (playerSize/3))
    pen.down()
    pen.setheading(-135)
    pen.forward(playerSize)
    pen.setheading(0)

def draw_x_or_o(x,y):
    global osPlaying
    if osPlaying:
        draw_O(x,y)
        osPlaying = False
    else:
        draw_X(x,y)
        osPlaying = True
    
def drawPlay(x,y):
    xPos = getXCoord(x)
    yPos = getYCoord(y)
    draw_x_or_o(xPos,yPos) 

def getXCoord(x):
    if x < -turtle.window_width() /2 + turtle.window_width() /3:
        return -turtle.window_width()/2 + turtle.window_width()/6
    elif x < -turtle.window_width() /2 + turtle.window_width() /3 * 2:
        return 0
    elif x < -turtle.window_width() /2 + turtle.window_width() /3 * 3:
        return turtle.window_width()/2 - turtle.window_width()/6

def getYCoord(y):
    if y > turtle.window_height()/2 - turtle.window_height()/3:
        return turtle.window_height()/2 - turtle.window_height()/6
    elif y > turtle.window_height()/2 - turtle.window_height()/3*2:
        return 0
    else:
        return -turtle.window_height()/2 + turtle.window_height()/6

draw_grid()
turtle.onscreenclick(drawPlay)

turtle.done()