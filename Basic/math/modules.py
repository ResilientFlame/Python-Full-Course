import math

# height = int(input('y: '))
# width = int(input('x: '))

# print(int(math.sqrt(height ** 2 + width ** 2)))

# distance = float(input('Введите расстояние до танка: '))
# angle = float(input('Введите угол в градусах: '))

# angle /= 57.2958
# x = math.cos(angle) * distance
# y = math.sin(angle) * distance

# print('Координаты вражеского танка:', x, ',', y)

# a = 5
# b = 5
# c = 5

# p = (a + b + c) / 2

# s = math.sqrt( p * ( p - a ) * ( p - b ) * ( p - c ) )

# print('Результат формулы Герона', s)

# x = int(input('Введите расстояние которую преодолел перс. по гориз.'))
# y = int(input('Введите расстояние которую преодолел перс. по верт.'))
# degree = float(input('Введите угол по которому двигался перс: '))
# degree /= 57.2958
# coordinates = [ x * math.cos(degree), y * math.sin(degree) ]

# print(coordinates)

# конвертер радианов в градусы:

# radians = float(input('Введите радианы: '))
# print('градусы:', math.degrees(radians))

# конвертер градусов в радианы:

# degrees = float(input('Введите градусы: '))
# print('радианы:', math.radians(degrees))

number = float(input('Введите вещественное число: '))

print('округляет вниз: ')
print(math.floor(number))
print('округляет вверх: ')
print(math.ceil(number))
print('берет модуль числа: ')
print(abs(number))
print('извлекает квадратный корень: ')
print(math.sqrt(number))
print('возводит экспоненту в степень, равную числу: ')
print(math.exp(number))
print('считает натуральный логарифм числа: ')
print(math.log(number))
print('считает логарифм числа по основанию 2: ')
print(math.log2(number))
print('считает логарифм числа по основанию 10: ')
print(math.log10(number))
print('считает синус и косинус числа: ')
print(math.sin(number), math.cos(number))