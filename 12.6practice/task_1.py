Number = int(input('Введите целое положительное число: '))

def summa_n(N):
    result = 0
    for i in range(1, N + 1):
        result += i
    print('Сумма чисел от 1 до', N, 'равна', result)

summa_n(Number)