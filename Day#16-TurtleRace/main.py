import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("steel blue")
user_bet = screen.textinput(title="Make your bet ", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

coor_y = -150
for i in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(i)
    new_turtle.goto(x=-280, y=coor_y)
    coor_y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You were right!!! {user_bet} turtle is the winner.")
            else:
                print(f"You were wrong {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()