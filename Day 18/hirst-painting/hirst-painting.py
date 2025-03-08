# import colorgram
#
# rgb_colors =[]
# colors = colorgram.extract('Methyl Phenylsulfoxide.jpg', 25)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen
import random

tutel = Turtle()
screen = Screen()
color_list = [(46, 92, 144), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47), (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16), (18, 96, 49), (211, 56, 76), (155, 23, 19), (187, 143, 156)]
screen.colormode(255)


tutel.setheading(225)
tutel.forward(300)
tutel.setheading(0)

dot_size = 20
spacing = 50
rows = 10
columns = 10


for row in range(rows):
    for col in range(columns):
        tutel.dot(dot_size, random.choice(color_list))
        tutel.forward(spacing)

    tutel.backward(columns * spacing)
    tutel.setheading(90)
    tutel.forward(50)
    tutel.setheading(0)

screen.exitonclick()