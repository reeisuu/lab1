import random

# Генерация случайного 6-значного числа
number = random.randint(100000, 999999)
print(f"Случайное число: {number}")

# Проверка, является ли число палиндромом
if str(number) == str(number)[::-1]:
    print("Это число является палиндромом!")
else:
    print("Это число не является палиндромом.")