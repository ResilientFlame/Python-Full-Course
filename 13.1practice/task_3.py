first_number = int(input('Введите число: '))
second_number = int(input('Введите второе число: '))

# сделан с рекурсивным подходом
def number_reverser (number, result = 0):
    result = result * 10 + number % 10
    number //= 10
    if number:
        return number_reverser(number, result)
    return result

first = number_reverser(first_number)
second = number_reverser(second_number)
print('Первое число наоборот:', first)
print('Второе число наоборот:', second)
print('Сумма:', first + second)

# С циклом питона
def fast_number_reverser(number):
    result = 0
    while number:
        result = result * 10 + number % 10
        number //= 10
    return result

print('Сумма наоборот:', fast_number_reverser(first + second))
