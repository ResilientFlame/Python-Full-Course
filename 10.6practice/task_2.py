enterNum = int(input('введите число: ')) + 1

for number in range(1, enterNum):
    integer = 0
    while integer < number:
        print(number, end=' ')
        integer += 1
    print()