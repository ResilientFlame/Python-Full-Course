levels = int(input('Введите кол-во уровней у пирамиды: '))
odd_number = 1
pyramid_final_len = 0

def decimal_counter(number):
    result = 0
    while number > 0:
        result += 1
        number //= 10
    return result

for level in range(levels):
    for odd in range(level + 1):
        if level == 4:
            pyramid_final_len += decimal_counter(odd_number)
            if odd < level:
                pyramid_final_len += 2
        odd_number += 2
odd_number = 1

for level in range(levels):
    string = ''
    for odd in range(level + 1):
        if odd < level:
            string += str(odd_number) + ' '
        else:
            string += str(odd_number)
        odd_number += 2
    
    emptyspc = pyramid_final_len - len(string) // 2
    print(' ' * emptyspc, end = ' ')
    print(string, end = '')
    print(' ' * emptyspc, end = ' ')
    print()