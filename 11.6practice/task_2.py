import math

count = int(input('Введите кол-во чисел: '))

for x in range(count):
    number = float(input('Введите вещественное число: '))
    # Если положительное число: 
    if abs(number) == number:
        ceiled = math.ceil(number)
        print('x =', ceiled, 'log(x)', math.log(ceiled))
        continue
    floored = math.floor(number)
    print('x =', floored, 'log(x)', math.exp(floored))