# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert_to_uppercase(string):
    uppercase_count = sum( 1 for char in string[:4] if char.isupper())
    if uppercase_count >= 2:
        return string.upper()
    else:
        return string

print(convert_to_uppercase("KAushik"))
