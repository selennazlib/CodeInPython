from turtle import Turtle, Screen
import random

tt = Turtle()
tt.shapesize(1)
tt.speed('fastest')

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tt.color(random_color())
        tt.circle(100)
        tt.setheading(tt.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()