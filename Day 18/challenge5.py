from turtle import Turtle,Screen
import random

turtol = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



turtol.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtol.color(random_color())
        turtol.circle(100)
        turtol.setheading(turtol.heading() + size_of_gap)


draw_spirograph(60)

screen.exitonclick()