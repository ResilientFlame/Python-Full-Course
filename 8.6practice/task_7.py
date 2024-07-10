# final_num = int(input('Введите N: '))
# res = 0
# for num in range(final_num):
#     elem = (-1) ** num * (1/2) ** num
#     res += elem

# print('ответ:',res)

# 12345
# robot
# 15243
# print('wfewf'.removeprefix('w'))

# qwerty
# qetyrw
# sandwiches
# 13579108642

word = input('Введите зашифрованное ( например: shacnidw ): ')

integer = 0
s = ''
e = ''

for element in word:
  if not (integer % 2):
    s += element
  else:
    e = element + e
  integer += 1

print ('расшифрованное слово: ' + s + e)

# akhmet
# atkehm
# qwerty
# qywter