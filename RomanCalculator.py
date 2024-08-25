roman_to_int_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
def roman_to_int(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_to_int_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
def int_to_roman(number):
    int_to_roman_map = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    result = ""
    for numeral, value in int_to_roman_map:
        while number >= value:
            result += numeral
            number -= value
    return result
total_sum = 0
while True:
    roman_input = input().strip()
    if roman_input == "+":
        break
    total_sum += roman_to_int(roman_input)
result = int_to_roman(total_sum)
print(result)
