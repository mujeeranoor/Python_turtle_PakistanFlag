import turtle
turtle.bgcolor("black")


def drawFillRectangle(x, y, length, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()


def drawStar(x, y, color, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for star in range(0, 5):
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()


def drawCircle(x, y, color, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def drawMoon(x, y, color, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


drawFillRectangle(-230, 125, 280, 460, 'dark green')
drawFillRectangle(-230, 125, 280, 130, 'white')
drawCircle(45, -100, 'white', 80)
drawMoon(65, -72, 'dark green', 70)
drawStar(70, 30, 'white', 50)


turtle.hideturtle()


turtle.done()
