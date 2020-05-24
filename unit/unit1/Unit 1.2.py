# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Введите время в секундах: "))
hours = int(time / 3600)
minutes = int((time - hours * 3600) / 60)
seconds = int((time - hours * 3600) - (minutes * 60))

print(hours, ":", minutes, ":", seconds)