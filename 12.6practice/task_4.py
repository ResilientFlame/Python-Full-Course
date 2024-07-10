def reversed_number(number):
    if number % 10:
        print(number % 10, end = '')
    if number // 10:
        reversed_number(number // 10)
    else:
        print()

counter = int(input('Сколько раз нужно выводить числа? '))

for count in range(counter):
    number = int(input('Введите целое число: '))
    print('Число наоборот', end = ' ')
    reversed_number(number)

print('Программа завершена!')