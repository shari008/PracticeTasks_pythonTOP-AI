# # 1 Celcius --> F, K
# celsius = float(input("Введите температуру в градусах Цельсия: "))

# fahrenheit = (celsius * 9 / 5) + 32
# kelvin = celsius + 273.15 
# print(f'{celsius}°C: {fahrenheit}°F')
# print(f'{celsius}°C: {kelvin} K')
      
# # 2
# n = int(input())
# if n%2==0:
#     print(f'{n} число четное')
# else:
#     print(f'{n} число нечетное')
# if n>0:
#     print(f'{n} число положительное')
# elif n==0:
#     print(f'{n} -- ноль')
# else:
#     print(f'{n} число отрицательное')
# if 10<=n<=50:
#     print(f'{n} число принадлежит диапозону [10;50]')
    
# 3 generator paroley
# import random
# import random
# import string

# def generate_password():
#     letters = [random.choice(string.ascii_uppercase) for _ in range(3)]
#     digits = [random.choice(string.digits) for _ in range(3)]
#     special_chars_list = "!@#$%^&*"
#     specials = [random.choice(special_chars_list) for _ in range(2)]
    
#     password_list = letters + digits + specials
    
#     random.shuffle(password_list)
    
#     password = "".join(password_list)
    
#     return password

# print(generate_password())


# 4
# def analyze_text():
    
#     text = input("Введите текст: ")
#     text_lower = text.lower()
   
#     char_counts = {}
#     for char in text_lower:
#         if char == ' ':
#             continue
    
#         if char in char_counts:
#             char_counts[char] += 1
#         else:
#             char_counts[char] = 1
            
#     sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
#     top_3 = sorted_chars[:3]

#     print("\n3 самых частых символа:")
#     for char, count in top_3:
#         print(f"'{char}' — встречается {count} раз(а)")

# analyze_text()

# 5
# def sieve_of_eratosthenes(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False

#     for i in range(2, int(n**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, n + 1, i):
#                 is_prime[j] = False

#     primes = [i for i in range(n + 1) if is_prime[i]]
#     return primes

# n = int(input('Введите значение N:'))
# print(f"Простые числа до {n}: {sieve_of_eratosthenes(n)}")

# 6
n = int(input())
s = ''
for i in range(1,n+1):
    s += (str(i))
print(s, s[n-1])