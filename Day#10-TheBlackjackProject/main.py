import random
import asciiart
from replit import clear


print(asciiart.cards)
def game():
    # Create a deal_card() function that uses the List below to *return* a random card.
    # 11 is the Ace.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []


    def deal_card():
        ran_num = random.choice(cards)
        return ran_num

    # create a function called calculate_score() that takes a list of cards as input ,and inside this func check for a blackjack (ace + 10) and return 0 instead of the actual score.
    def calculate_score(playing_cards):
        if sum(playing_cards) == 21 and len(user_cards) == 2:
            return 0

        if 11 in playing_cards and sum(playing_cards) > 21:
            playing_cards.remove(11)
            playing_cards.append(1)

        return sum(playing_cards)

    def compare(user_score, comp_score):
        if user_score == comp_score:
            return "Draw"
        elif comp_score == 0:
            return "Blackjack!!! Computer win"
        elif user_score == 0:
            return "Blackjack!!! User win"
        elif user_score == 21:
            return "User win"
        elif comp_score == 21:
            return "Computer win"
        elif user_score > 21:
            return "Computer win"
        elif comp_score > 21:
            return "User win"
        elif user_score > comp_score:
            return "User win"
        else:
            return "Computer win"


    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    is_game_over = False
    while not is_game_over:
        # if the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"    user cards are : {user_cards} and user's score is : {user_score}\n")
        print(f"    computer cards are : {computer_cards} and computer's score is : {comp_score}\n")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("\nWant to draw another card ?")
            if draw_card == 'no':
                is_game_over = True
            elif draw_card == 'yes':
                user_cards.append(deal_card())

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    """print(f"    user cards are : {user_cards} and user's score is : {user_score}\n")
    print(f"    computer cards are : {computer_cards} and computer's score is : {comp_score}\n")"""
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack ?") == 'yes':
    clear()
    game()







