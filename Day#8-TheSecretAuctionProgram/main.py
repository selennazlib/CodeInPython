# this program aims to find the highest bid value
# create an empty dict
d = {}

go_on = True
while go_on:
    keys = input("What is your name?: ")
    values = int(input("What's your bid?: $"))
    d[keys] = values
    is_continue = input("Are there any other bidders? Type 'yes' or 'no' ")
    if is_continue == "no":
        go_on = False

def winner():
    key_list = list(d.keys())
    value_list = list(d.values())
    max_value = max(value_list)
    position = value_list.index(max_value)
    winner_name = key_list[position]
    print(f"The winner is {winner_name} with a bid of ${max_value}")

winner()