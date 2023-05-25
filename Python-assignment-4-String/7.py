# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def replace_not_poor(string):
    not_index = string.find('not')
    poor_index = string.find('poor')
    if poor_index > not_index and not_index != -1 and poor_index != -1:
        return string[:not_index] + 'good' + string[poor_index + 4:]
    else:
        return string

string1 = "The lyrics is not that poor!"
string2 = "The lyrics is poor!"

print(replace_not_poor(string1))
print(replace_not_poor(string2))

