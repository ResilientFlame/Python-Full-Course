# 0.0012 -> 1.2e-3

user_number = float(input('Введите любое число: '))

def transcendentConv (number):
    manticca = 0
    while number >= 10 or number < 1:
        if number >= 10:
            number /= 10
            manticca += 1
        else:
            manticca -= 1
            number = number * 10
    return str(number) + 'e' + str(manticca)

print(transcendentConv(user_number))