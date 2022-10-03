# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

my_list = []
n = 156
if n == 1:
    my_list.append(1)
elif n == 2:
    my_list.append(1)
    my_list.append(0)
else:
    while n != 0:
        if n % 2 != 0:
            my_list.append(1)
        else:
            my_list.append(0)
        n = n // 2
i = 0
while i < len(my_list):
    print(my_list[i], end='')
    i += 1
