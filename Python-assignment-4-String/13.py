# 13. Write a Python program to check whether a string starts with specified characters.


def starts_with(str, character):
    return str.startswith(character)


print(starts_with('Python', "p"))
print(starts_with('Python', "P"))