def shifr_cesar(string, x):

    ru_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    en_lower = 'abcdefghijklmnopqrstuvwxyz'
    en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    answer = []
    
    for char in string:
        if char in ru_lower:
            old_index = ru_lower.index(char)
            new_index = (old_index + x) % len(ru_lower)
            answer.append(ru_lower[new_index])
            
        elif char in ru_upper:
            old_index = ru_upper.index(char)
            new_index = (old_index + x) % len(ru_upper)
            answer.append(ru_upper[new_index])
            
        elif char in en_lower:
            old_index = en_lower.index(char)
            new_index = (old_index + x) % len(en_lower)
            answer.append(en_lower[new_index])
            
        elif char in en_upper:
            old_index = en_upper.index(char)
            new_index = (old_index + x) % len(en_upper)
            answer.append(en_upper[new_index])
            
        else:
            answer.append(char)
            
    return "".join(answer)

text = input('Введите текст - ')
key = int(input('Введите ключ шифра - '))
encrypted = shifr_cesar(text, key)
decrypted = shifr_cesar(encrypted, -key)

print(f"Оригинал: {text}")
print(f"Зашифровано (сдвиг {key}): {encrypted}")
print(f"Расшифровано: {decrypted}")