# 16. Write a Python program to print the index of the character in a string.


def print_character_indexes(string):
    for index, char in enumerate(string):
        print(char, index)

string = "kaushik"
print_character_indexes(string)

