# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
def fun(num1, num2):
    try:
        num1, num2 = float(num1), float(num2)
        answer = num1 / num2
    except ValueError:
        return "ошибка"
    except ZeroDivisionError:
        return "делить на ноль нельзя!"
    return answer
