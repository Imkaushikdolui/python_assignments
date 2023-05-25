# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number(Digits should not be repeated). For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1250
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.

import random


def generate_four_digit_number():
    digits = random.sample(range(10), 4)
    random_num = ''.join(map(str, digits))
    return random_num


number = generate_four_digit_number()


def calculate_cows_and_bulls(guess_number):
    cows = 0
    bulls = 0
    for i in range(0, 4):
        if guess_number[i] == number[i]:
            cows += 1
        elif guess_number[i] in number:
            bulls += 1
    return cows, bulls


def game():
    print(number)
    cow = 0
    guesses = 1
    while cow < 4:
        user_number = input("Guess the number: ")
        cow, bull = calculate_cows_and_bulls(user_number)
        print("Cows:", cow, "bulls:", bull)

        if cow == 4:
            print("Congratulations!! You guessed the number:",
                  number, "in", guesses, "guesses")
        else:
            guesses += 1


game()