levels = int(input('Введите число: '))

for level in range(1, levels + 1):
    for letter in range(1, levels + 1):
        if letter <= level:
            print(letter, end = '')
        else:
            print('.', end = '')
    for letter in range(levels, 0, -1):
        if letter <= level:
            print(letter, end = '')
        else:
            print('.', end = '') 
    print()