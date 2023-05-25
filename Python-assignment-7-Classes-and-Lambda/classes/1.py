# 1) Write a python class to convert an integer into a roman numeral and viceversa

class RomanNumeralConverter:
    def __init__(self):
        self.numeral_map = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

    def to_roman(self, num):
        roman = ''
        for symbol, value in self.numeral_map.items():
            while num >= value:
                roman += symbol
                num -= value
        return roman

    def from_roman(self, roman):
        num = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in self.numeral_map:
                num += self.numeral_map[roman[i:i+2]]
                i += 2
            else:
                num += self.numeral_map[roman[i]]
                i += 1
        return num

converter = RomanNumeralConverter()
print(converter.to_roman(800))
print(converter.from_roman('DCCC'))


