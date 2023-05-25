# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input("Enter the quantity: "))
unit_cost = 100
total_cost = quantity * unit_cost

if total_cost > 1000:
    discount = 0.1 * total_cost
    total_cost -= discount

print("Total cost:", total_cost)
