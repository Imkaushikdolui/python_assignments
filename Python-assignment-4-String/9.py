# 9. Write a Python program to remove the nth index character from a nonempty string.

def remove_index(string, index):
    new_string = string[:index] + string[index+1:]
    return new_string

print(remove_index("kaushik",4))
