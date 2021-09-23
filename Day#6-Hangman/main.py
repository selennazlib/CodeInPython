import random
import word_list
import hangman_stages
# or --> from hangman_stages import stages
# randomly choose a word from the list
chosen_word = random.choice(word_list.word_list)

# Create an empty list called display, for each letter in the chosen word , add a "_" to 'display'
display = ["_"]*len(chosen_word)

# create a variable called 'lives' to keep track of the number of lives left  set lives to equal 6 bc there are 6 stages
lives = 6
#print logo
print(hangman_stages.logo)
# Use a while loop to let the user guess again
# get the input and check the letter
end_of_game = False
while not end_of_game:
    # Ask the user to guess a letter (make guess lowercase)
    guess = input("Guess a letter: ").lower()
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        # Check if the letter the user guessed is one of the letters in the chosen word.
        if letter == guess:
            display[index] = guess
            print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the chosen word !!!")

    # stages for hangman
    if lives == 6:
        print(hangman_stages.stages[-1])
    elif lives == 5:
        print(hangman_stages.stages[-2])
    elif lives == 4:
        print(hangman_stages.stages[-3])
    elif lives == 3:
        print(hangman_stages.stages[-4])
    elif lives == 2:
        print(hangman_stages.stages[-5])
    elif lives == 1:
        print(hangman_stages.stages[-6])
    else:
        end_of_game = True
        print("You lose")
    # OR print(hangman_stages.stages[lives])
    if "_" not in display:
        print("You win")
        end_of_game = True




