# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n1 = int(input('введите число: '))
n2 = -n1
list = []
for i in range(n2, n1):
    list.append(i)
print(list)

list2 = []
n3 = int(input('сколько чисел нужно найти: '))
i = 0
while i < n3:
    list2.append(int(input(f'введите позицию номер {i + 1}: ')))
    i = i + 1
e = 0
a = 1
while e < n3:
    a = a * list[list2[e]-1]
    e = e + 1
print(a)


