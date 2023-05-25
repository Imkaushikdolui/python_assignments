# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string

has_uppercase = lambda string: any(char.isupper() for char in string)
has_lowercase = lambda string: any(char.islower() for char in string)
has_digit = lambda string: any(char.isdigit() for char in string)
has_minimum_length = lambda string: len(string) >= 10

input_string = "PaceWisd0m"

if all(x(input_string) for x in [has_uppercase, has_lowercase, has_digit, has_minimum_length]):
    print("Valid string")
else:
    print("Invalid string")


