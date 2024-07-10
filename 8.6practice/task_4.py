# позиции:
x = 6
y = 19

# North - W keyboard
# South - S keyboard
# West - A keyboard
# East - D keboard

while x <= 15 and y <= 20:
    print('[Программа]: Марсоход находится на позиции ' + str(x) + ',' + str(y) + ' введите команду:')
    control = input('[Оператор]: ')
    if control == 'A' and x >= 0:
        x -= 1
    elif control == 'D' and x <= 15:
        x += 1
    elif control == 'W' and y <= 20:
        y += 1
    elif control == 'S' and y >= 0:
        y -= 1
