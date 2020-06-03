# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def fun(num1, num2, num3):
    try:
        string = [num1, num2, num3]
        string.pop(string.index(min(string)))
        return sum(string)
    except TypeError:
        return "невозможно"


print(fun(11, 2, 13))
