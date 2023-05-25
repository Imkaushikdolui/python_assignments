# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

numbers = []
while True:
    num = int(input("Enter an integer number (0 to finish): "))
    if num == 0:
        break
    numbers.append(num)

sum = sum(numbers)
average = sum / len(numbers)

print("Sum:", sum)
print("Average:", average)
