# 8. Write a Python function that takes a list of words and returns the length of the longest one. 

def longestword(words):
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length

words = ["apple","ball","cat"]
print(longestword(words))
