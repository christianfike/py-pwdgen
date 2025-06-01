import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '?', '@', '_',]

print("\nWelcome to the Password Generator!")
path = str(input("Default or custom password generator? (d/c)\n"))


if path.lower() == 'd' or path.lower() == 'default':
    print("\nUsing default password generator. (20 characters long with the use of numbers and symbols)")

    ## Getting random letters, symbols, and numbers
    nr_numbers = random.randint(1, 4)
    nr_symbols = random.randint(1, 4)
    nr_letters = 20 - (nr_symbols + nr_numbers)

    random_letters = random.sample(letters, nr_letters)
    random_numbers = random.sample(numbers, nr_numbers)
    random_symbols = random.sample(symbols, nr_symbols)

    password = random_letters + random_numbers + random_symbols

    ## Creating the password and printing it
    random.shuffle(password)
    random.shuffle(password)

    print("\nRandomly generated password: ", end='')
    for character in password:
        print(character, end='')

    print("\n")



elif path.lower() == 'c' or path.lower() == 'custom':
    print("\nUsing custom password generator.")

    ## Getting user input
    nr_letters = int(input("\nHow many letters would you like in your password? (0-52)\n"))
    nr_numbers = int(input("How many numbers would you like? (0-10)\n"))
    nr_symbols = int(input("How many symbols would you like? (0-14)\n"))
    



    ## Getting random letters, symbols, and numbers based on user input
    random_letters = random.sample(letters, nr_letters)
    random_numbers = random.sample(numbers, nr_numbers)
    random_symbols = random.sample(symbols, nr_symbols)

    password = random_letters + random_numbers + random_symbols


    ## Creating the password and printing it
    random.shuffle(password)
    random.shuffle(password)

    print("\nRandomly generated password: ", end='')
    for character in password:
        print(character, end='')

    print("\n")