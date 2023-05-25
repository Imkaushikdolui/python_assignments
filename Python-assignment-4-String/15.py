# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2


def count_repeated_characters(string):
    repeated_characters = {}
    for char in string:
        if string.count(char) > 1:
            repeated_characters[char] = string.count(char)
    return repeated_characters


Samplestring = 'thequickbrownfoxjumpsoverthelazydog'
print(count_repeated_characters(Samplestring))