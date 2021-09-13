import random

user_chose = int(input("What do you choose ?  Type 0 for rock, 1 for Paper ,or 2 for Scissors."))
comp_chose = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps_list = [rock, paper, scissors]

print("Your chose :\n")

if user_chose == 0:
    print(rps_list[user_chose])
elif user_chose == 1:
    print(rps_list[user_chose])
elif user_chose == 2:
    print(rps_list[user_chose])

print("Computer chose :\n")

if comp_chose == 0:
    print(rps_list[comp_chose])
elif comp_chose == 1:
    print(rps_list[comp_chose])
elif comp_chose == 2:
    print(rps_list[comp_chose])


#compare
if comp_chose == user_chose:
    print("Drawn")
elif comp_chose == 0: #rock
    if user_chose == 2:
        print("You lose!")
    else:
        print("You win!")
elif comp_chose == 1: #paper
    if user_chose == 2:
        print("You win!")
    else:
        print("You lose!")
elif comp_chose == 2: #scissors
    if user_chose == 0:
        print("You Win!")
    else:
        print("You lose!")