# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = int(input("Введите целое число: "))
temp = number
length = 0

while temp != 0:
    temp = int(temp / 10)
    length = length + 1

number1 = (number + number * 10 ** length)
number2 = (number1 * 10 ** length + number)
sum=number + number1 + number2

print(number, "+", number1, "+", number2 ,"=", sum )
