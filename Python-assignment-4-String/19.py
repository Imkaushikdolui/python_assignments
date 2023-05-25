# 19. Write a Python program to find smallest and largest word in a given string.

def smallest_largest_word(str):
    words = str.split()
    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)
    return "smallest word : "+smallest_word, "largest word : "+largest_word

string = "lorem ipsum dolor sit amet"

print(smallest_largest_word(string))