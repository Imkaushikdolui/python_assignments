# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.



# Question 17
numbers = list(range(1, 101))
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Question 18
divisible_by_4 = [num for num in even_numbers if num % 4 == 0]
divisible_by_6 = [num for num in even_numbers if num % 6 == 0]
divisible_by_8 = [num for num in even_numbers if num % 8 == 0]
divisible_by_10 = [num for num in even_numbers if num % 10 == 0]

divisible_by_3 = [num for num in odd_numbers if num % 3 == 0]
divisible_by_5 = [num for num in odd_numbers if num % 5 == 0]
divisible_by_7 = [num for num in odd_numbers if num % 7 == 0]
divisible_by_9 = [num for num in odd_numbers if num % 9 == 0]

print("Even numbers divisible by 4:", divisible_by_4)
print("Even numbers divisible by 6:", divisible_by_6)
print("Even numbers divisible by 8:", divisible_by_8)
print("Even numbers divisible by 10:", divisible_by_10)

print("Odd numbers divisible by 3:", divisible_by_3)
print("Odd numbers divisible by 5:", divisible_by_5)
print("Odd numbers divisible by 7:", divisible_by_7)
print("Odd numbers divisible by 9:", divisible_by_9)

