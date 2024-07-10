Number = int(input('Введите целое число: '))
print('0 - найти сумму его чисел. 1 - найти наибольшую среди его цифр. 2 - найти наименьшую.')
action = int(input('Укажите что нужно сделать: '))

def number_sum(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    print('Сумма его цифр:', result)

def maximum(number):
    result = 0
    while number > 0:
        if number % 10 > result:
            result = number % 10
        number //= 10
    print('Наибольшая цифра:', result)

def minimum(number):
    result = number % 10
    number //= 10
    while number > 0:
        if number % 10 < result:
            result = number % 10
        number //= 10
    print(result)

if not(action):
    number_sum(Number)
elif action == 1:
    maximum(Number)
elif action == 2:
    minimum(Number)
else:
    print('Wtf.')
    print('Можно ввести только 0, 1, 2 но не остальные.')