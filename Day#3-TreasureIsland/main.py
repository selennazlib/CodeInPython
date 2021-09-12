#this is a fun game which helps to learn if/elif/else statements.

print('''
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          \
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..bmw-�
                  ```''''���                  ~ \n\n''')

print("\nWelcome to the Treasure Island.\nYour mission is to find the treasure.\n")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if direction == 'left':
    state = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if state == 'wait':
        colour = input("You arrive at the island unharmed . There is a house with 3 doors. One RED, one YELLOW ,and one BLUE. Which colour do you choose?\n")
        if colour == 'YELLOW':
            print("You Win!!")
        elif colour == 'RED':
            print("Burned by fire. Game over")
        elif colour == 'BLUE':
            print("Eaten by beasts. Game over")
        else:
            print("Game over.")
    else:
        print("Attacked by trout . Game Over")

else:
    print("Fall into a hole. Game over.")