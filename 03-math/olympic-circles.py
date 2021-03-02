import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(.5)

size = turtle.numinput("Olympic Circles", "Size (1 - 10):", 5, 1, 10)
pen.pensize(size*2)

ringWidth = size * 15
ringRadius = ringWidth /2
spacing = ringWidth / 4
logoWidth = ringWidth * 3 + spacing * 2
logoWidthBottom = ringWidth * 2 + spacing

#left blue circle
pen.up()
pen.setpos(-logoWidth /2 + ringRadius, ringRadius/2 - spacing/8)
pen.down()
pen.color("blue")
pen.circle(ringRadius)

#middle black circle
pen.up()
pen.setpos(0, ringRadius/2 - spacing/8)
pen.down()
pen.color("black")
pen.circle(ringRadius)

#right red circle
pen.up()
pen.setpos(logoWidth /2 - ringRadius,ringRadius/2 - spacing/8)
pen.down()
pen.color("red")
pen.circle(ringRadius)

#left orange circle
pen.up()
pen.setpos(-logoWidthBottom /2 + ringRadius, -ringRadius/2 + spacing/8)
pen.down()
pen.color("orange")
pen.circle(ringRadius)

#right green circle
pen.up()
pen.setpos(logoWidthBottom / 2 - ringRadius, -ringRadius/2 + spacing/8)
pen.down()
pen.color("green")
pen.circle(ringRadius)


turtle.done()