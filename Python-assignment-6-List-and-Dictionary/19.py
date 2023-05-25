# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

new_list = [list(i) for i in set(tuple(sublist) for sublist in my_list)]

print(new_list)