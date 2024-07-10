string = 'qwerty  Kamina Simon lavascriptt'
last = 0
current = 0

for letter in string + ' ':
    if letter != ' ':
        current += 1
    else:
        if current > last:
            last = current
        current = 0
print('Самое длинное слово, ' + str(last) + ' букв')