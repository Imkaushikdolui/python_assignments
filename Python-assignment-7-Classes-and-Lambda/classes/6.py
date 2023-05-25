# 6) Write a Python class to implement pow(x, n) 

class PowerCalculator:
    def power(self, x, n):
        return x ** n

calc = PowerCalculator()
print(calc.power(2, 2))