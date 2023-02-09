import turtle

import time

import random

# Set up the screen

wn = turtle.Screen()

wn.title("Snake Game")

wn.bgcolor("green")

wn.setup(width=600, height=600)

wn.tracer(0)

# Snake head

head = turtle.Turtle()

head.speed(0)

head.shape("square")

head.color("black")

head.penup()

head.goto(0,0)

head.direction = "stop"

# Snake food

food = turtle.Turtle()

food.speed(0)

food.shape("circle")

food.color("red")

food.penup()

food.goto(0,100)

# Snake body segments

segments = []

# Function to move the snake

def move():

    if head.direction == "up":

        y = head.ycor()

        head.sety(y + 20)

    if head.direction == "down":

        y = head.ycor()

        head.sety(y - 20)

    if head.direction == "left":

        x = head.xcor()

        head.setx(x - 20)

    if head.direction == "right":

        x = head.xcor()

        head.setx(x + 20)

# Function to change direction

def go_up():

    head.direction = "up"

def go_down():

    head.direction = "down"

def go_left():

    head.direction = "left"

def go_right():

    head.direction = "right"

# Keyboard bindings

wn.listen()

wn.onkeypress(go_up, "Up")

wn.onkeypress(go_down, "Down")

wn.onkeypress(go_left, "Left")

wn.onkeypress(go_right, "Right")

# Main game loop

while True:

    wn.update()

    # Check for collision with the food

    if head.distance(food) < 20:

        # Move the food to a random spot

        x = random.randint(-290, 290)

        y = random.randint(-290, 290)

        food.goto(x,y)

        # Add a segment to the snake

        new_segment = turtle.Turtle()

        new_segment.speed(0)

        new_segment.shape("square")

        new_segment.color("grey")

        new_segment.penup()

        segments.append(new_segment)

    # Move the end segments first

    for index in range(len(segments)-1, 0, -1):

        x = segments[index-1].xcor()

        y = segments[index-1].ycor()

        segments[index].goto(x, y)

    # Move segment 0 to where the head is

    if len(segments) > 0:

        x = head.xcor()

        y = head.ycor

