#julianna disalvo
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encode(password):
    if len(password) > 8:
        print("Password is too long")

    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit

    return encoded_password



while True:
    menu()
    menu_input = int(input("Please enter an option: "))

    if menu_input == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!\n")

    elif menu_input == 2:
        print(f"The encoded password is {encode(password)}, and the orginal password {decoder(encoded_password)}.\n")

    elif menu_input == 3:
        break