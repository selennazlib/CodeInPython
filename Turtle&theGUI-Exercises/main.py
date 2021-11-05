from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("DarkSlateGrey")

# draw a square
"""
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
"""
# dashed line
"""
for i in range(4):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
"""
colors = ["blue", "green", "yellow", "purple", "pink", "cyan", "coral", "lavender", "sienna"]
"""
# 360 / edge of the shape


def dif_shapes(edge):
    for i in range(edge):
        angle = 360 / edge
        my_turtle.forward(75)
        my_turtle.right(angle)

for edge_of_shape in range(3, 11):
    dif_shapes(edge_of_shape)
    my_turtle.color(random.choice(colors))
"""
my_turtle.pensize(10)
my_turtle.speed('fast')
def random_walk():
    for i in range(50):
        my_turtle.right(random.randint(0, 4) * 90)
        my_turtle.forward(20)
        my_turtle.color(random.choice(colors))
random_walk()
screen = Screen()
screen.exitonclick()
