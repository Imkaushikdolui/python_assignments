# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white


def unique_words(words):
    word_list = words.split(", ")
    unique_words = sorted(set(word_list))
    result = ", ".join(unique_words)
    return result

a = "red, white, black, red, green, black"
print(unique_words(a))

