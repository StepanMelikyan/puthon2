# Реализуйте алгоритм перемешивания списка
import random

n1 = int(input('введите длину списка: '))

list = []
for i in range(1, n1 + 1):
    list.append(i)
print(list)

i = 0
for i in list:
    b = random.randint(0, len(list) - 1)
    list[i-1], list[b] = list[b], list[i-1]

print(list)