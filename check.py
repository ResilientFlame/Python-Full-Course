

# for i in range(1, 10, 2):
#     pass

# print(i)


# цикл for обьявляет переменную доступная к внешнему коду в случае если оно заработает.
# i = 99

# for i in range(1, 10, -2):
#     i += 2

# print(i)

# n = 5
# cipher_count = 0
# for _ in range(n):
#     new_number = int(input("Введите число: "))
#     while new_number:
#         if new_number % 10 > 5:
#             cipher_count += 1
#         new_number //= 10
# else:
#     print(cipher_count)

def check():
    value = 9
    while value > 5:
        if value == 6:
            return value
        value -= 1

print(check())