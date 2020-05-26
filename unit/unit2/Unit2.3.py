# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input("Введите месяц в цифрах: "))
if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
elif month == 12:
    print("Winter")
elif month >= 1 or month <= 2:
    print("Winter")
else:
    print("такого месяца не существует")
