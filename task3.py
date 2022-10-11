# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

numbers = [1, 2, 2, 3, 3, 4, 5, 7, 7, 7, 8, 15]


list = []
unique_numbers = set(numbers)

for number in unique_numbers:
    list.append(number)
print(list)