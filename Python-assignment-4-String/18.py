# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

def swap(str):
    return str.replace(",",".")


string = "32.054,23"
print(swap(string))

