from turtle import Turtle, Screen
import random

# how we got the color_list
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_col = (r, g, b)
#     rgb_colors.append(new_col)
#
# print(rgb_colors)

color_list = [(229, 225, 221), (218, 229, 220), (233, 220, 226), (218, 223, 230), (230, 207, 91), (225, 149, 91), (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145)]


my_turtle = Turtle()
my_turtle.speed('fastest')
my_turtle.up()
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.forward(250)
my_turtle.setheading(0)

my_turtle.down()

number_of_dots = 100

screen = Screen()
screen.colormode(255)

def draw():
    for dot in range(1, number_of_dots + 1):
        random_color = random.choice(color_list)
        my_turtle.penup()
        my_turtle.dot(10, random_color)
        my_turtle.forward(50)

        if dot % 10 == 0:
            my_turtle.setheading(90)
            my_turtle.forward(50)
            my_turtle.setheading(180)
            my_turtle.forward(500)
            my_turtle.setheading(0)

draw()

screen.exitonclick()