import pandas as pd
import turtle


IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

game_is_on = True
data = pd.read_csv("50_states.csv")
states_column = data["state"].to_list()

guessed_list = []

while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"Score : {len(guessed_list)} / 50 ", prompt="What's another state's name? ")
    answer_state = answer_state.title()

    if answer_state == 'Exit':
        break

    if answer_state in states_column:
        guessed_list.append(answer_state)
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        state_data = data[data.state == answer_state]
        my_turtle.goto(int(state_data.x), int(state_data.y))
        # convert x and y to integer to avoid getting an error. They're strings!!!!!
        my_turtle.write(answer_state)
        # avoiding to print extra unnecessary lines and to print only the name of state
        """
        turtle.write(state_data.state.item()) it's the alternative way to get name of state
        """



