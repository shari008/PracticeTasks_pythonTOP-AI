def print_pack_report(x):
    if x%3==0 and x%5==0:
        print(f"{x} - расфасуем по 3 или по 5")
    elif x%3==0 and x%5!=0:
        print(f"{x} - расфасуем по 3")
    elif x%3!=0 and x%5==0:
        print(f"{x} - расфасуем по 5")
    else: print(f"{x} - не заказываем!")
x = int(input())
print_pack_report(x)
