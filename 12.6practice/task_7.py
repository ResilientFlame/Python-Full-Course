# Для реалистичной игры
import random


def main_menu():
    print('Игры:')
    print('Камень, ножницы, бумага')
    print('Угадай число')
    choose = int(input('Выберите игру ( 1-ая либо 2-ая ): '))
    if choose == 1:
        first_game()
    elif choose == 2:
        second_game()
    else:
        print('Выберите одну из этих игр')
        main_menu()

def first_game():
    print('Камень - 0, ножницы - 1, бумага - 2')
    choose = int(input('Выберите одну: '))
    bot_choose = random.randint(0, 2)
    if choose < 0 or choose > 2:
        print('Такого предмета в игре нету.')
        first_game()
    else:
        code__of__first__game(choose, bot_choose)

def code__of__first__game(choose, bot_choose):
    if not(choose) and bot_choose == 2:
        # Слова бота
        print('Bot: Бумага!')
        print('Вы проиграли.')
        first_game()
    elif not(choose) and bot_choose == 1:
        # Слова бота
        print('Bot: Ножница!')
        print('Вы выиграли')
        first_game()
    elif not(choose) and not(bot_choose):
        # Слова бота
        print('Bot: Камень!')
        print('Играем заново')
        first_game()
    elif choose == 1 and bot_choose == 2:
        # Слова бота
        print('Bot: Бумага!')
        print('Вы выиграли')
        first_game()
    elif choose == 1 and bot_choose == 1:
        # Слова бота
        print('Bot: Ножницы!')
        print('Играем заново')
        first_game()
    elif choose == 1 and not(bot_choose):
        # Слова бота
        print('Bot: Камень!')
        print('Вы проиграли')
        first_game()
    elif choose == 2 and bot_choose == 2:
        # Слова бота
        print('Bot: Бумага!')
        print('Играем заново')
        first_game()
    elif choose == 2 and bot_choose == 1:
        # Слова бота
        print('Bot: Ножницы!')
        print('Вы проиграли')
        first_game()
    elif choose == 2 and not(bot_choose):
        # Слова бота
        print('Bot: Камень!')
        print('Вы выиграли')
        first_game()

def second_game():
    lowest = 0
    average = 50
    highest = 100
    print('Загадайте число между 1 и 100')
    while True:
        print('Ваше число больше либо меньше', average, '?')
        answer = int(input('0 - меньше, 1 - больше, 2 - равняется '))
        if not(answer):
            highest, average = average, (average + lowest) // 2
        elif answer == 1:
            lowest, average = average, (highest + average) // 2
        elif answer == 2:
            print('Вы загадали число', average)
            break
        else:
            second_game()

main_menu()