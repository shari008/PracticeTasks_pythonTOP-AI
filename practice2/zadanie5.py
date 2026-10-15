roman_numbers = ['IX', 'IV', 'XLII', 'XCIX', 'MMXXIII']

nums = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def convert_roman_to_int(roman_numbers):
    result = []
    for roman in roman_numbers:
        num = 0
        for i in range(len(roman)):
            value = nums[roman[i]]
            if i + 1 < len(roman) and value < nums[roman[i + 1]]:
                num -= value
            else:
                num += value
        result.append(num)
    return result

res = convert_roman_to_int(roman_numbers)

for i in range(len(res)):
    print(f'{roman_numbers[i]} --> {res[i]}')