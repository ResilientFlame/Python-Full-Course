f_letter = input('Буква которую хотите найти в тексте: ')
number = input('Цифра в тексте: ')

def count_letters(string):
    letters = 0
    numbers = 0
    for letter in string:
        if letter.lower() == f_letter.lower():
            letters += 1
        elif letter == number:
            numbers += 1
    print('Количество цифр ' + number + ':', numbers)
    print('Количество букв ' + f_letter + ':', letters)

count_letters('987664321')
