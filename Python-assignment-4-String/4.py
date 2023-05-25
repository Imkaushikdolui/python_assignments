# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def replace_first_character(str):
    first_char = str[0]
    replaced_string = first_char + str[1:].replace(first_char, '$')
    return replaced_string

print(replace_first_character("restart"))
