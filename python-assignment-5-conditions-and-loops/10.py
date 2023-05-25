# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = float(input("Enter the salary: "))
years_of_service = int(input("Enter the years of service: "))

if years_of_service > 5:
    bonus = 0.05 * salary
    net_bonus = salary + bonus
    print("Net bonus amount:", net_bonus)
else:
    print("No bonus.")
