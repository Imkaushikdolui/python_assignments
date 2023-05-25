# 20. Write a Python program to remove all consecutive duplicates of a given string.

def duplicates(string):
    result = ""
    for char in string:
        if result == "" or char != result[-1]:
            result += char
    return result

print(duplicates("kkkaaauussshhiikk"))