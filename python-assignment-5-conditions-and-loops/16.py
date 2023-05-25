# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
my_list = [10, 20, 30, 40, 50]
search_num = int(input("Enter a number to search and delete: "))

if search_num in my_list:
    my_list.remove(search_num)

print("Updated list:", my_list)
