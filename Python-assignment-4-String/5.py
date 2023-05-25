# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

def swap(string1, string2):
    swapped_string1 = string2[:2] + string1[2:]
    swapped_string2 = string1[:2] + string2[2:]
    result = swapped_string1 + " " + swapped_string2
    return result

# Example usage
string1 = "abc"
string2 = "xyz"
print(swap(string1, string2))
