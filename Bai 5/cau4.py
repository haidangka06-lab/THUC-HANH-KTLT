class RomanToInteger:
    def __init__(self):
        self.roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    def roman_to_int(self, roman):
        total = 0
        prev_value = 0
        for ch in reversed(roman):
            value = self.roman_values[ch]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
converter = RomanToInteger()
print("Số La Mã 'XIV' =", converter.roman_to_int("XIV"))
print("Số La Mã 'MCMXCIV' =", converter.roman_to_int("MCMXCIV"))

