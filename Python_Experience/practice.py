# // - точно работает как Math.floor на JavaScript

# print (81 // 8) 
# print (91 % 10)

# Номера домов и квартир

# number_request = int (input ('Введите номер квартиры и дома: '))

# print ('Номер квартиры: ', number_request // 10)
# print ('Номер дома ', number_request % 10)

# first_num = int (input ('Введите число дохода первого квартала '))
# second_num = int (input ('Введите число дохода второго квартала '))
# third_num = int (input ('Введите число дохода третьего квартала '))
# firth_num = int (input ('Введите число дохода четвертого квартала '))

# first_res = first_num + second_num
# second_res = third_num + firth_num

# print (first_res / second_res)

# leg_size = int (input ('Укажите размер катета: '))
# res = leg_size * 2 // 2

# print (res)

# request_minute = int (input ('Укажите число минут: '))

# req_hours = request_minute // 60
# req_minutes = request_minute % 60

# if request_minute >= 60:
#     print (req_hours, 'hours and', req_minutes, 'minutes!')
# else: 
#     print (req_minutes, 'minutes!')

# first_number = int (input ('Введите первое число '))
# second_number = int (input ('Введите второе число '))
# res = first_number % 100 + second_number % 100

# print (res)

# four_value_number = int (input ('Укажите рандомное 4-значное число: '))

# first_num = four_value_number // 1000
# second_num = (four_value_number % 1000) // 100
# third_num = (four_value_number % 100) // 10
# firth_num = four_value_number % 10

# print (first_num)
# print (second_num)
# print (third_num)
# print (firth_num)

# number = str (4556)

# for i in number:
#     print (i)

# a, b = b, a

# number = 1783

# print (number % 10)
# print (number % 100 // 10)
# print (number // 100 % 10)
# print (number // 1000)

# def solution (number):
#     result = 0
#     for i in range (1, number + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
    
#     return result

# print (solution (9))

# Питон может считать в обратном порядке!

# fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']

# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])
# print(fruits[-4])

# def Reversed_Number (number):
#     number_list = list (str (number))
#     reversed_list = list (reversed (number_list))
    
#     return int (''.join (reversed_list))

# print (Reversed_Number (9397))

# def deepArray (denth, length):
#     if (denth < 1): return []
#     result = []
#     for i in range (1, length + 1):
#         result.append (deepArray (denth - 1, length))
#     return result

# print (deepArray (2, 2))

# def to_weird_case(words):
#     words = words.split (' ')
#     for i in range (len (words)):
#         current = list (words[i])
#         integer = 0
#         while (integer < len (current)):
#             if integer % 2 == 0:
#                 current[integer] = current[integer].upper ()
#                 integer += 1
#                 continue
#             current[integer] = current[integer].lower ()
#             integer += 1
#         words[i] = ''.join (current)
#     return ' '.join (words)
# print (to_weird_case ('LLLLLLLL'))


# def flattenArray (WrongArray):
#     result = []
#     for object in WrongArray:
#         if (type (object) is list):
#             for i in flattenArray (object): result.append (i)
#             continue
#         result.append (object)
#     return result

# print (flattenArray ([[4, 5, 6, 7, 9], [3, 38, 48, 28, 49], [[4, 4, 2, 48]]]))

# def deepCount (array):
#     result = len (array)
#     for element in array:
#         if (type (element) == list):
#             result += deepCount (element)
#     return result

# print (deepCount ([3, 4, 2, 39, 48, 2, 3, [3, 2, 9, 4, 2, [82, 92, 47, 39]]]))

# def arrayDenth (array):
#     container = []
#     if len (array) > 1:
#         for element in array:
#             arrayDenth (element)
#     elif (len (container) < 1):
#         container.append (1)
#     else:
#         container[-1] += 1
        
#     return container

# print (arrayDenth ([[], [], []]))

# def ArrayTest (number, array):
#     if (number > 0):
#         array.append (number - 1)
#         ArrayTest (number - 1, array)
#     return array
    
# print (ArrayTest (4, []))

# def deepArray (array, result):
#     for element in array:
#         innerDenth = deepArray (element, result + 1)
#         print (innerDenth)
#     return result

# print (deepArray ([[], [], []], 0))

# def two_value_task (first, second, array):
    
    
# print (two_value_task (3, 3, [[], [], []]))

# StartDenth нужен для того чтобы наш result постоянно не увеличевался,
# Если присмотреться, то можно заметить что условии позволяют сблизиться к этому событию.
# Задача 24.04.2023, повторить, понять, сделать похожую задачу, и опять повторить ✔✔✔

# def badPractice (array, level):
#     for element in array:
#         innerDenth = badPractice (element, level + 1)
#         if level < innerDenth:
#             level = innerDenth
#     return level
    
# print (badPractice ([[], [], []], 0))

# def simpleCount (array, denth):
#     if (len (array) > 0): 
#         innerValue = simpleCount (array[0], denth + 1)
#         return innerValue
#     return denth

# print (simpleCount ([[[]]], 0))

# https://go.skillbox.ru/education/my
# gmail: alimalikuly@gmail.com
# password: Ali@008877

# print('Sweater Weather')

# current = 9
# last = 15

# def factorial (num):
#     if num == 1: return 1
#     return num + factorial (num - 1)

# while current <= last:
#     print(factorial(current))
#     current += 1

# def evenNums (n):
#     result = []
#     for i in range(1, n // 2 + n % 2):
#         result.append((i * 2) ** 3)
#     return result

# print(evenNums(13))


# def oddNum (n):
#     odd = 1
#     while odd + 2 < n:
#         print(odd)
#         odd += 2
#     return odd

# print(oddNum(5))

# first temp.

# def oddNum (n):
#     odd = 1
#     while odd < n:
#         print(odd)
#         odd += 2
#     return odd

# print(oddNum(7))

# second temp.

# def oddWord (word):
#     res = ''
#     for i in range(len(word)):
#         if i % 2 == 0: res += word[i]
#     return word + ' -> ' + res

# print(oddWord('Hypocrisy'))

# def toWeirdCase (string):
#     idx = 0
#     result = ''
#     for item in string:
#         if item == ' ': 
#             idx = -1
#         elif idx % 2 == 0: 
#             item = item.upper()
#         else:
#             item = item.lower()
#         result += item
#         idx += 1
#     return result

# print(toWeirdCase(' dream   core'))

# word = list('lolkekjo')
# word[0] = word[0].upper ()
# print(''.join(word))

# def evenCube (n):
#     q = 0
#     arr = []
#     if n % 2 > 0: q = 1
#     for i in range(1, n // 2 + q):
#         arr.append(i * 2)
#     return arr

# print(evenCube(15))

# def evens (n):
#     for i in range(1, n // 2 + n % 2):
#         print(i * 2)

# print(evens(7))

# def evens (n):
#     for i in range(1, n // 2 + n % 2):
#         print(i * 2)

# evens(9)

# def microwave (sec):
#     for i in reversed(range(1, sec + 1)):
#         print(i)

# microwave(9)

# def microwave (sec):
#     for i in range(sec, 9, 2):
#         print(i)

# microwave(8)

# def evens (n):
#     res = []
#     for i in range(n - n % 2, 0, -2):
#         res.append(i)
#     return res

# print(evens(11))

# def evens (n):
#     res = []
#     el = 2
#     if n % 2: el = 1
#     for i in range(n - el, 0, -2):
#         res.append(i)
#     return res;

# print(evens(14))

# def evens (n):
#     result = []
#     start = lambda num: num - 2 if not(num % 2) else num - 1
#     for even in range(start(n), 0, -2):
#         result.append(even)
#     return result

# print(evens(11))

# def countdown (num):
#     for count in range(num - num % 2, 0, -2):
#         print(count)

# countdown(10)
# begin = 5
# for i in range(begin + begin % 2, 10, 2):
#     print(i)

# def NumGuess (num):
#     if num % 2: return str(num) + ' is Odd!'
#     return str(num) + ' is Even!'

# print(NumGuess(17))


# age = int(input('Сколько вам лет? '))
# def condition_ (user):
#     if user < 18: print('Несовершеннолетним подросткам не рекомендуется данный контент!')
#     elif user < 60: print('Добро Пожаловать!')
#     else:
#         print('Вам точно хочется зайти на этот сайт???')

# condition_(age)

# print( 10 % 2 == False )


# def odds(n):
#     start = n - 1 if not(n % 2) else n - 2
#     result = []
#     for even in range(start, 0, -2):
#         result.append(even)
#     return result

# print(odds(14))

print('567' * 5)