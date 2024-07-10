print('# задание: нужно указать количество чисел, затем написать их')
numbers = int(input('Введите количество чисел: '))
result = []

for integer in range(numbers):
    number = int(input('Укажите то самое число: '))
    count = 0
    for devider in range(1, number):
        if not(number % devider):
            count += 1
    if count == 1:
        result.append(number)

print('количество простых чисел внутри указанных вами числах: ')
print(len(result))