# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x = input('введите число: ')
array = []
for i in range(len(x)):
    array.append(x[i])
array2 = []
array2 = [int(e) for e in array]
print(sum(array2))