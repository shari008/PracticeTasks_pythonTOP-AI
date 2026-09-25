# 1 Celcius --> F, K
celsius = float(input("Введите температуру в градусах Цельсия: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15 
print(f'{celsius}°C: {fahrenheit}°F)')
print(f'{celsius}°C: {kelvin} K')
      
# 2
n = int(input())
if n%2==0:
    print(f'{n} число четное')
else:
    print(f'{n} число нечетное')
if n>0:
    print(f'{n} число положительное')
elif n==0:
    print(f'{n} -- ноль')
else:
    print(f'{n} число отрицательное')
if 10<=n<=50:
    print(f'{n} число принадлежит диапозону [10;50]')