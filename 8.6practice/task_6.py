# prices = int(input('Введите расходы на проживание: '))
# educational_grant = int(input('Введите стипендию: '))
# result_money = 0

# for month in range(1, 11):
#     integer, fraction = prices // 1, prices - (prices // 1)
#     # prices - educational_grant = сумма долгов
#     # result_money = сумма текущих долгов.
#     prices = integer + (fraction // 0.1) / 10
#     result_money += prices - educational_grant
#     print('месяц траты ' + str(prices) + ' не хватает ' + str(result_money))
#     prices = prices * 103 / 100

# print('Нужно попросить у родителей ' + str(result_money) + ' рублей')

# # print(12360.0 * 103 / 100)


stalls = input('Введите чертежь стойл с буквами "a" и "b" (a - свободное стойло, b - занятое)')
# stalls = 'abbbbbb'
litr = 2
result = 0
for stall in stalls:
    if stall == 'b':
        result += litr
    litr += 2
print(str(result) + ' молока за день!')