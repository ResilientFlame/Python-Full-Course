rows = int(input('Введите кол-во рядов: '))
seat = int(input('Введите кол-во сидении в рядах/ряде: '))
distance = int(input('Введите кол-во метров между рядами: '))

for i in range(rows):
    print('=' * seat, '*' * distance, '=' * seat)