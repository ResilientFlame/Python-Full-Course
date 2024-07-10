numbers = [ 34, 77, 1, 8 ]
biggest = 0
result_num = 0

for number in numbers:
    num_sum = 0
    integer = number
    while integer > 0:
        num_sum += integer % 10
        integer //= 10
    if num_sum > biggest:
        result_num = number
        biggest = num_sum

print('Наибольшее число:', result_num)
print('сумма его цифр:', biggest)