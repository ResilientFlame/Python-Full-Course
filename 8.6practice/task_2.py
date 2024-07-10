message_ = input('Написать сообщение ')
position = 1

for symbol in message_:
    if symbol == '*':
        print('Символ «*» стоит на позиции ' + str(position))
        break
    position += 1
