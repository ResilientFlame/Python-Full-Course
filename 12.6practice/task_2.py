def positive():
    print('Положительное')

def negative():
    print('Отрицательное')

def test():
    number = float(input('Введите число: '))
    if number == abs(number):
        positive()
    else:
        negative()

test()