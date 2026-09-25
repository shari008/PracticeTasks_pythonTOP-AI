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
import random
import random
import string

def generate_password():
    letters = [random.choice(string.ascii_uppercase) for _ in range(3)]
    digits = [random.choice(string.digits) for _ in range(3)]
    special_chars_list = "!@#$%^&*"
    specials = [random.choice(special_chars_list) for _ in range(2)]
    
    password_list = letters + digits + specials
    
    random.shuffle(password_list)
    
    password = "".join(password_list)
    
    return password

print(generate_password())
