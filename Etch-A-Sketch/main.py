from turtle import Turtle, Screen

tt = Turtle()
tt.color('purple')
tt.speed('fastest')
screen = Screen()

def move_forward():
    tt.forward(20)

def move_backward():
    tt.backward(20)

def counter_clockwise():
    tt.left(20)

def clockwise():
    tt.right(20)

def clear():
    tt.clear()
    tt.penup()
    tt.home()
    tt.pendown()

screen.listen()
# listens for screen / window inputs.
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="e", fun=clear)
screen.exitonclick()
