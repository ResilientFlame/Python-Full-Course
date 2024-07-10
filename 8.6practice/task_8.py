# def palindrom (text):
#     for i in range(len(text) // 2 + 1):
#         current = ''.join(list(reversed(text[0:i+1])))
#         integer = 0
#         boolean = False
#         print(current, text[i+1:])
#         for letter in text[i+1:]:
#             if current[integer] == letter:
#                 boolean = True
#                 integer += 1
#             else:
#                 boolean = False

# print(palindrom('кабак'))

# def palindrom (text):
#     new_line = ''
#     new_line_reverse = ''
#     for i in text:
#         new_line = new_line + i
#         new_line_reverse = i + new_line_reverse
    
#     if new_line == new_line_reverse:
#         return new_line, new_line_reverse
#     return 'Нет это не палиндром.'

# print(palindrom('наворован'))

text = 'наворован'
new_line_reverse = ''
for i in text:
    new_line_reverse = i + new_line_reverse

if new_line_reverse == text:
    print('Да, это палиндром!')
else:
    print('Нет, это не палиндром!')
