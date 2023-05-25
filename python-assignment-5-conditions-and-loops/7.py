# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
count = 0
for num in numbers:
    if num > 30:
        count += 1
print("Count:", count)
