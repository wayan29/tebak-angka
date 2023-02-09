import turtle

def draw_apple_logo(turt):

    turt.color("#FF1C1C")

    turt.begin_fill()

    turt.circle(50)

    turt.end_fill()

    turt.penup()

    turt.goto(0, 50)

    turt.pendown()

    turt.color("#FFFFFF")

    turt.begin_fill()

    turt.circle(25)

    turt.end_fill()

t = turtle.Turtle()

t.speed(0)

draw_apple_logo(t)

turtle.done()

