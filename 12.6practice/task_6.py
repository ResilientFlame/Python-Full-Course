# def BigGeneralDevider(first, second):
#     smallest = min(first, second)
#     BiggestDevider = 0
#     for devider in range(1, smallest + 1):
#         if not(first % devider) and not(second % devider):
#             BiggestDevider = devider

#     BiggestDevider

# first_number = int(input('Введите первое число: '))
# second_number = int(input('Введите второе число: '))
# BigDevider = BigGeneralDevider(first_number, second_number)

# print('Наибольший делитель:', BigDevider)

# def gcd (result, zero):
#     while zero:
#         print(result, zero)
#         result, zero = zero, result % zero
#     result

# first = int(input('Введите первое число: '))
# second = int(input('Введите второе число: '))

# print('Наибольшии общий делитель:', gcd(first, second))

# def gcd(a,b):
#     while a and b:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     print(a, b)

# gcd(79, 66)