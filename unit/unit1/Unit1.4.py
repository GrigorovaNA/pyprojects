# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max = 0
while number != 0:
    temp = number % 10
    if temp > max:
        max = temp
    number = number // 10
print(max)
