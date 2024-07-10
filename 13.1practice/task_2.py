import math

def dot_remover (number):
    if not(number % 1):
        number = int(number)
    return number

def maximum_of_two(first, second):
    return (first + second + abs(first - second)) / 2

def maximum_of_three (first, second, third):
    first_res = maximum_of_two(first, second)
    final_res = maximum_of_two(first_res, third)
    # Убираем точку если после нее только ноль.
    final_res = dot_remover(final_res)
    return final_res


first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))
third = float(input('Введите третье число: '))

print(maximum_of_three(first, second, third))
