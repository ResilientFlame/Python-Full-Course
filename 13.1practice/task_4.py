def numCounter(number):
    counter = 0
    while number:
        counter += 1
        number //= 10
    return counter

def changeNumber(number, count):
    count -= 1
    first_digit = number // (10 ** count)
    between_digit = (number % (10 ** count) // 10) * 10
    last_digit = number % 10
    return (last_digit * (10 ** count)) + between_digit + first_digit

def main():
    firstN = int(input('Введите первое число: '))
    firstC = numCounter(firstN)
    if firstC > 2:
        firstN = changeNumber(firstN, firstC)
        print('Измененное число:', firstN)
        secondN = int(input('Введите второе число: '))
        secondC = numCounter(secondN)
        if secondC > 3:
            secondN = changeNumber(secondN, secondC)
            print('Измененное второе число:', secondN)
            print('\n Сумма измененных чисел:', firstN + secondN)
            
        else:
            print('Во втором числе кол-во чисел меньше 4-рех.')
    else:
        print('В первом числе кол-во чисел меньше 3-рех')

main()