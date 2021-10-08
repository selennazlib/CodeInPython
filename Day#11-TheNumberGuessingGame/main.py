# import libs
import logo
import random

print(logo.logo)

is_over = False

def difficulty(difficulty_of_game):
    if difficulty_of_game == 'easy':
        live = 10
    elif difficulty_of_game == 'hard':
        live = 5
    print(f"You have {live} attempts remaining to guess the number")
    while live > 0:
        user_num = int(input("Make a guess: "))
        if CHOSEN_NUM > user_num:
            print("Too low")
            live -= 1
            print(f"You have {live} attempts remaining to guess the number")
        elif CHOSEN_NUM < user_num:
            print("Too high")
            live -= 1
            print(f"You have {live}  attempts remaining to guess the number")
        else:
            print(f"You got it !! The answer is  {user_num}")
            exit()

while not is_over:
    # allow the users choose numbers between 1-100
    CHOSEN_NUM = random.randint(1, 100)
    # To cheat run the code below:
    """print(f"chosen number is: {CHOSEN_NUM}")"""
    difficult = input("Chose a difficulty . Type 'easy' or 'hard' ")
    difficulty(difficult)
    ask_again = input("Would you like to try it again? : ")
    if ask_again == 'no':
        is_over = True
