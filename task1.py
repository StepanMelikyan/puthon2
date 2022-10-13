# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('введите текст: ').split()
print(text)
i = 0

while i < len(text):
    if "абв" in text[i]:
        del text[i]
    i += 1
print(text)