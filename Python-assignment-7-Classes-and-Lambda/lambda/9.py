# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 

original_list = ['red', 'black', 'white', 'green', 'orange']
search_element = "ack"

contains_substring = lambda string: search_element in string

result = list(filter(contains_substring, original_list))

print("Elements of the original list that contain the specific substring:")
print(result)

