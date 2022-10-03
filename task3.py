# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_list2 = []
i = 0
while i < len(my_list):
    if my_list[i] % 1 != 0:
        my_list2.append(my_list[i] % 1)
    i += 1
print(my_list2)

e = 0
min1 = my_list2[0]
while e < len(my_list2):
    if min1 > my_list2[e]:
        min1 = my_list2[e]
    e += 1

x = 0
max1 = my_list2[0]
while x < len(my_list2):
    if max1 < my_list2[x]:
        max1 = my_list2[x]
    x += 1
print(max1 - min1)
