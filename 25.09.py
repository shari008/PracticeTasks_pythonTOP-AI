# 1

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