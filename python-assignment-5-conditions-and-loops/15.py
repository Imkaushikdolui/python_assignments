# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

numbers = []
while True:
    num = input("Enter an integer (press 'q' to quit): ")
    if num == 'q':
        break
    numbers.append(int(num))

if numbers:
    average = sum(numbers) / len(numbers)
    product = 1
    for num in numbers:
        product *= num
    print("Average:", average)
    print("Product:", product)
else:
    print("No numbers entered.")
