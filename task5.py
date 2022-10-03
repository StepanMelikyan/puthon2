# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = 8

my_list = [0, 1]

e = 0
while e < k - 1:
    my_list.append(1)
    e += 1
my_list[k] = 0

i = k
while i < 2 * k:
    my_list.append(my_list[i-1] + my_list[i])
    i += 1

x = k
while x > -1:
    my_list[x] = my_list[x + 2] - my_list[x + 1]
    x -= 1


print(my_list)