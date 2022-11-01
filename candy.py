# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
import random
import emoji
from time import sleep
from light_progress.commandline import ProgressBar


def progress():
    n = 42
    with ProgressBar(n) as progress_bar:
        for item in range(n):
            sleep(0.01)
            progress_bar.forward()


candy = 67
max_take = 28 #максимальное кол-во конфет которое можно забрать за один ход
first_move = random.randint(1, 2)


count1 = 0 #колличество шагов первого игрока
count2 = 0 #колличество шагов второго игрока


move1 = 0 #сколько забирает за шаг первый игрок
move2 = 0 #сколько забирает за шаг второй игрок

message = ["Если вы хотите играть против игрока введите '1', если хотите играть против бота, то введите '2'"]
choice = int(input(f'{message}: '))
print(emoji.emojize('отличный выбор :thumbs_up:'))

if choice == 1:
    player1 = input('введите Ваше имя: ')
    player2 = input('введите Ваше имя: ')

    while candy != 0:
        if first_move == 1:
            count1 += 1
            print(f"{emoji.emojize(':man:')} ходит {player1} ")
            move1 = int(input(f'сколько конфет хотите забрать за {count1} шаг?-'))
            if move1 > max_take:
                print(f"{emoji.emojize(':raised back of hand:')} можно забрать максимум {max_take} кофет за один ход")
            else:
                candy = candy - move1
            first_move = 2
        else:
            count2 += 1
            print(f"{emoji.emojize(':person:')} ходит {player2}")
            move2 = int(input(f'сколько конфет хотите забрать за {count2} шаг?-'))
            if move2 > max_take:
                print(f"{emoji.emojize(':raised back of hand:')} можно забрать максимум {max_take} кофет за один ход")
            else:
                candy = candy - move2
            first_move = 1


        if candy < max_take:
            max_take = candy
        print(f'осталось {candy} конфет')

    if first_move == 1:
        if count1 > count2:
            print(f"{emoji.emojize(':man:')} {emoji.emojize(':star_struck:')} победил {player1} сделав {count1} шага")
        if count2 == count1:
            print(f"{emoji.emojize(':person:')} {emoji.emojize(':star_struck:')} победил {player2} сделав {count2} шага")
    if first_move == 2:
        if count2 > count1:
            print(f"{emoji.emojize(':person:')} {emoji.emojize(':star_struck:')} победил {player2} сделав {count2} шага")
        if count2 == count1:
            print(f"{emoji.emojize(':man:')} {emoji.emojize(':star_struck:')} победил {player1} сделав {count1} шага")

else:
    player = input('введите Ваше имя: ')
    while candy != 0:
        if first_move == 1:
            count1 += 1
            print(f"{emoji.emojize(':person:')} ваш ход")
            move1 = int(input(f'сколько конфет хотите забрать за {count1} шаг?-'))
            if move1 > max_take:
                print(f"{emoji.emojize(':raised back of hand:')} можно забрать максимум {max_take} кофет за один ход")
            else:
                candy = candy - move1
            first_move = 2
        else:
            count2 += 1
            progress()
            print(f"{emoji.emojize(':robot:')} ходит бот ")
            if candy > max_take * 2:
                move2 = random.randint(1, max_take)
            elif max_take + 1 < candy <= max_take * 2:
                move2 = candy - 29
            elif candy == max_take + 1:
                move2 = 1
            else:
                move2 = candy

            print(f"{emoji.emojize(':robot:')} бот за {count2} шаг забирает {move2} конфет")
            candy = candy - move2
            first_move = 1

        print(f'осталось {candy} конфет')
        if candy < max_take:
            max_take = candy

    if first_move == 1:
        if count1 > count2:
            print(f"{emoji.emojize(':person:')} {emoji.emojize(':star_struck:')} Поздравляю! Вы победили сделав {count1} шага")
        if count2 == count1:
            print(f"{emoji.emojize(':robot:')} {emoji.emojize(':expressionless_face:')} победил бот сделав {count2} шага")
    if first_move == 2:
        if count2 > count1:
            print(f"{emoji.emojize(':robot:')} {emoji.emojize(':expressionless_face:')} победил бот сделав {count2} шага")
        if count2 == count1:
            print(f"{emoji.emojize(':person:')} {emoji.emojize(':star_struck:')} Поздравляю! Вы победили сделав {count1} шага")





