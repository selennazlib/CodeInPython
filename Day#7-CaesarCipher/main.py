alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_on = True
while go_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text_str, shift_num, direction_ed):
        text_list = []
        text_list[: 0] = text_str
        if direction_ed == "encode":
            for i in range(len(text_list)):
                shifted_ind = alphabet.index(text_list[i]) + shift_num
                text_list[i] = alphabet[shifted_ind]
            print(f"The encoded text is: {''.join(text_list)}")
        elif direction_ed == "decode":
            for i in range(len(text_list)):
                shifted_ind = alphabet.index(text_list[i]) - shift_num
                text_list[i] = alphabet[shifted_ind]
            print(f"The decoded text is: {''.join(text_list)}")

    caesar(text, shift, direction)

    is_continue = input("Would you like to continue ? : ").lower()
    if is_continue == "no":
        go_on = False
