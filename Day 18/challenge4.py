import turtle
from turtle import Turtle, Screen
import random

turtil = Turtle()
screen = Screen()
turtle.colormode(255)

def random_color():
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)

    return (random_red, random_green, random_blue)

colors = ["red", "orange", "yellow", "blue", "indigo", "violet"]
directions = [0, 90, 180, 270]
turtil.pensize(10)
turtil.speed("fastest")

for _ in range(1000000000000000):
    turtil.color(random_color())
    turtil.forward(30)
    turtil.setheading(random.choice(directions))

screen.exitonclick()
