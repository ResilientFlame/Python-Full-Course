import math

first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))

summa = first + second
diferrence = abs(first - second)

print('Самая наибольшая цифра:', int(diferrence + summa) // 2)