import random
print('''
                                                                                                                                                                                               _                                                                 
                                                   | |                                             _                  
 ____    ____   ___   ___  _ _ _   ___    ____   _ | |    ____   ____  ____    ____   ____   ____ | |_    ___    ____ 
|  _ \  / _  | /___) /___)| | | | / _ \  / ___) / || |   / _  | / _  )|  _ \  / _  ) / ___) / _  ||  _)  / _ \  / ___)
| | | |( ( | ||___ ||___ || | | || |_| || |    ( (_| |  ( ( | |( (/ / | | | |( (/ / | |    ( ( | || |__ | |_| || |    
| ||_/  \_||_|(___/ (___/  \____| \___/ |_|     \____|   \_|| | \____)|_| |_| \____)|_|     \_||_| \___) \___/ |_|    
|_|                                                     (_____|                                                       
                                                                                                                                           
''')


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator\n")
hm_letters = int(input("How many letters would you like in your password?\n"))
hm_numbers = int(input("How many numbers would you like in your password?\n"))
hm_symbols = int(input("How many symbols would you like in your password?\n"))

password = " "

for i in range(0, hm_letters):
    password += random.choice(letters)
for i in range(0, hm_numbers):
    password += random.choice(numbers)
for i in range(0, hm_symbols):
    password += random.choice(symbols)

print(password)





