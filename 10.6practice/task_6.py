height = int(input('Укажите высоту пирамиды: '))
final = height + height - 1

for integer in range(1, height + 1):
    hash_count = integer + integer - 1
    max_count = hash_count
    for line in range(1, final + 1):
        if line > ( final - max_count ) // 2 and hash_count > 0:
            print('#', end = '')
            hash_count -= 1
            continue
        print(' ', end = '')
    print()