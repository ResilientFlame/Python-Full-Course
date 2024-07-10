import random

word = [ 'кровать', 'спать', 'блять' ][ random.randint(0, 2) ]
print(word)

width = len(word) # int(input('Введите ширину прямоугольника кол-вом горизонтальных символов: '))
height = 6 # int(input('Введите высоту прямоугольника кол-вом символов: '))

for vertical in range(height):
    print('|', end = '')
    for horizontal in range(width):
        if not(vertical) or (vertical == height - 1):
            print('-', end = '')
        else:
            print(word[horizontal], end = '')
    print('|')