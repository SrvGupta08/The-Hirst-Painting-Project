# Extract the colours from the image using Cologram

import colorgram
import turtle
import random

colors = colorgram.extract(r'G:\My Drive\Python\100 days Python\Day 18\Hirst Painting Project\image.jpg', 63)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

colors_list = [(215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56), (11, 87, 108), (177, 190, 213), (111, 124, 153), (81, 142, 169), (73, 63, 53)]

timbu = turtle.Turtle()
turtle.colormode(255)
timbu.hideturtle()
timbu.speed("fastest")

timbu.penup()
timbu.setheading(215)
timbu.forward(350)
timbu.setheading(0)

for j in range(10):
    for i in range(10):
        timbu.dot(20, random.choice(colors_list))
        timbu.forward(50)

    timbu.left(90)
    timbu.forward(50)
    timbu.left(90)
    timbu.forward(500)
    timbu.setheading(0)

screen = turtle.Screen()
screen.exitonclick()