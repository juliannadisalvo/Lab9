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
        new_digit = str((int(digit) + 3))
        encoded_password += new_digit

    return encoded_password

def decode(encoded_password):
    decoded_passwordList = []
    for i in range (0, len(encoded_password)):
        decoded_passwordList.append(int(encoded_password[i])-3)
        decoded_passwordList[i] = (str(decoded_passwordList[i]))
    return ''.join(decoded_passwordList)



while True:
    menu()
    menu_input = int(input("Please enter an option: "))

    if menu_input == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!\n")

    elif menu_input == 2:
        print(f"The encoded password is {encoded_password}, and the orginal password {decode(encoded_password)}.\n")

    elif menu_input == 3:
        break