from turtle import Turtle, Screen
import random

tammy = Turtle()
screen = Screen()
tammy.shape("turtle")

colors = ["red", "orange", "yellow", "blue", "indigo", "violet"]


def draw_shape(number_side):
    angle = 360 / number_side
    for _ in range(number_side):
        tammy.forward(100)
        tammy.right(angle)

for shape_side_number in range(3, random.randint(4, 100)):
    tammy.color(random.choice(colors))
    draw_shape(shape_side_number)

screen.exitonclick()