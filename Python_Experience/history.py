# array = [
#     [
#         [], [], [[[]]]
#     ],
#     [
#         [], [], []
#     ],
#     [
#         [], [], []
#     ]
# ]

# Правило в програмировании:
# Если определенная часть / строка / итерация кода еще не закончилось
# то код после нее не будет работать!
# Нужно изменить мышление в програмировании,
# Все тут работает по-очереди...

# def simpleRecourse (array):
#     for element in array:
#         simpleRecourse (element)
#         print (element)
    
# simpleRecourse (array)

# Max Denth

# def deepArray (array, result):
#     result_number = result
#     # Цикл работает в тот момент когда условия правильные 🧠
#     for element in array:
#         innerCount = deepArray (element, result + 1)
#         if innerCount > result_number: result_number = innerCount
#     return result_number
    
# print (deepArray (array, 0))

# def duplicate_encode (word):
#     word = list (word.lower ())
#     keys = []
#     elementIndex = 0
#     for element in word:
#         if not (element in keys): 
#             keys.append (word.index (element))
#             continue
#         while (elementIndex > -1):
#             elementIndex = word.index (element, elementIndex)
#             word[elementIndex] = ')'
        

# print (duplicate_encode ('Success'))

# def duplicate_encode (word):
#     word = list (word.lower ())
#     result = ''
#     reminder = []
#     for integer in range (len (word)):
#         current = word [integer]
#         if (current in reminder):
#             result += ')'
#         else:
#             try:
#                 word.index (current, integer + 1)
#             except ValueError:
#                 result += '('
#             else:
#                 reminder.append (current)
#                 result += ')'
    
#     return result

# print (duplicate_encode ('success'))
# def duplicate_encode (word):
#     word = list (word.lower ())
#     result = ''
#     reminder = []
#     for integer in range (len (word)):
#         element = word [integer]
#         if element in reminder:
#             result += ')'
#             continue
#         try: word.index (element, integer + 1)
#         except: result += '('
#         else:
#             reminder.append (element)
#             result += ')'

#     return result

# print (duplicate_encode ('Success'))

# def uniqueSymbols (word):
#     word = list (word)
#     result = False
#     for integer in range (len (word)):
#         current = word [integer]
#         try:
#             word.index (current, integer + 1)
#         except:
#             result = True
#             break
#         else:
#             result = False
#             break
#     return result

# print (uniqueSymbols ('edge'))

# def uniqueSymbols (word):
#     word = list (word)
#     reminder = []
#     result = True
#     for element in word:
#         if element in reminder:
#             result = False
#             break
#         reminder.append (element)
#     return result

# print (uniqueSymbols ('edge'))

# def makeUnique (array):
#     result = []
#     for element in array:
#         if element in result:
#             continue
#         result.append (element)
    
#     return result
    
# print (makeUnique ([4, 5, 6, 7, 4]))

# def unique_even_numbers (array):
#     result = []
#     for element in array:
#         if element % 2 == 0 and not (element in result):
#             result.append (element)
#         elif element in result:
#             return False
#     return True

# print (unique_even_numbers ([4, 6, 8]))

# def uniqueWords (words):
#     reminder = []
#     for element in words:
#         element = element.lower ()
#         if element in reminder:
#             return False
#         reminder.append (element)
    
#     return True
    
# print (uniqueWords (['lf', 'Lf', 'LF']))

# def uniqueSymbols (symbols):
#     reminder = []
#     result = []
#     for element in symbols:
#         if element in reminder:
#             result.append (element)
#             continue
#         reminder.append (element)
    
#     return result
    
# print (uniqueSymbols ([4, 5, 6, 4, 6]))

# def onlyUnique (symbols):
#     result = []
#     for element in symbols:
#         if element in result:
#             continue
#         result.append (element)
#     return result

# print (onlyUnique ([4, 5, 4, 6, 3]))


# def is_prime (num):
#   integer = 1
#   while (integer <= num):
#     if num % integer > 0 and num > 1:
#       integer += 1
#     elif integer < num and integer > 1:
#       return False
#   return True

# print (is_prime (5))

# def unique_numbers (numbers):
#     reminder = []
#     result = []
    
#     for integer in range (len (numbers)):
#         current = numbers [integer]
#         try:
#             numbers.index (current, integer + 1)
#         except:
#             if not (current in reminder): result.append (current)
#         else:
#             reminder.append (current)
#     return result

# print (unique_numbers ([4, 53, 53, 4, 3, 9, 17]))

# [4, 4, 3, 6, 8]

# def find_uniq(arr):
#     s = set(arr)
#     for e in s:
#         if arr.count(e) == 1:
#             return e
# print (find_uniq ([9, 4, 3, 5]))

# arr = [4, 5, 3, 4]
# object = set (arr)

# def create_phone_number (n):
#     form = list ('(xxx) xxx-xxxx')
#     index = 0
#     for integer in range (len (form)):
#         current = form [integer]
#         if current == 'x':
#             form [integer] = str (n [index])
#             index += 1
#     return ''.join (form)

# create_phone_number ([3, 4, 2, 6, 4, 5, 3, 4, 3, 4])

# def to_weird_case (words):
#     words = list (words)
#     index = 0
#     integer = 0
#     while integer < len (words):
#         element = words [integer]
#         if element == ' ': 
#             while (words [integer] == ' '): integer += 1
#             index = 0
#         if index % 2 > 0: words [integer] = words [integer].lower ()
#         else:
#             words [integer] = words [integer].upper ()
#         index += 1
#         integer += 1
#     return ''.join (words)

# sorry for ugly code (((

# print (to_weird_case ('wEiRd   string'))

# изменение integer в for

# def to_weird_case (words):
#     words = list (words)
#     index = 0
#     for integer in range (len (words)):
#         if words [integer] == ' ':
#             integer += 1
#             index = 0
#             continue
#         elif index % 2 == 0: words [integer] = words [integer].upper ()
#         else:
#             words [integer] = words [integer].lower ()
#         index += 1
#     return ''.join (words)

# print (to_weird_case ('DREAM    CORE 👁'))

# client_request_time = int (input ('Введите время когда хотите получить посылку'))
# if (client_request_time >= 8 and client_request_time <= 10) or (client_request_time >= 12 and client_request_time <= 18) or (client_request_time >= 20 and client_request_time < 22):
#   print('Можно получить посылку')
# else:
#   print('Посылку получить нельзя')


# number = 1234
# sum = 0
# while number > 0:
#   if number % 10 == 5:
#     break
#   sum += number % 10
#   number = number // 10

# print (sum)

# sum = 0
# inputMoney = 0

# while (inputMoney < 10000):
#   inputMoney = int (input ('Дай деньги Лебовский!) '))
#   cubNum = int (input ('Число кубика '))
#   if (inputMoney > 10000): break
#   if cubNum != 3: sum += inputMoney
#   else: 
#     sum = 0
#     print ('Ло-о-o-о-ох!')
#     break

# print (sum)

# randomNumber = int (input ('Введите рандомное число чтобы найти ее куб '))
# result = 0
# integer = 1

# while integer < 3:
#   if result == 0: 
#     result = randomNumber * randomNumber
#   else:
#     result = result * randomNumber
  
#   integer += 1

# print (result)

# givenNumber = 5
# lowest = 0
# middle = 50
# highest = 100
# attempt = 0

# while True:
#     attempt += 1
#     question = int(input('Твое число равно, меньше или больше, чем ' + str(middle)))
    
#     if question == 3:
#         highest = middle
#         middle = (highest + lowest) // 2
#     elif question == 1:
#         print('Вы загaдали число', middle)
#         break
#     elif question == 2:
#         lowest = middle
#         middle = (highest + lowest) // 2

# print ('Число попыток:', attempt)


# artists_list = [ 'abcdifg', 'abcd', 'abcdi', 'abcdi', 'abc' ] 

# def wordSorting (artists):
#     for index in range (1, len (artists)):
#         current = artists [index]
#         i = index - 1
#         while i >= 0:
#             if len (current) < len (artists [i]):
#                 artists [i + 1] = artists [i]
#                 artists [i] = current
#                 i -= 1
#             else:
#                 break
    
#     return artists

# print (wordSorting (artists_list))

# artists_list = [ 'analog_mannequin', 'antent', 'oneheart', 'reidenshi', 'willix' ]

# def insertion_sort (artists):
#     for index in range (1, len (artists)):
#         current = artists [index]
#         i = index - 1
#         while i >= 0:
#             if len (artists [i]) > len (current):
#                 artists [i + 1] = artists [i]
#                 artists [i] = current
#                 i -= 1
#             else:
#                 break
    
#     return artists

# print (artists_list)
# print (insertion_sort (artists_list))


# artists_list = [ 'Kute', 'MC ORSEN', 'Green Orxnge', 'Kordhell',
# 'DVRST', 'PLAYAMANE' ]

# def insertion_sort (artists):
#     for index in range (1, len (artists)):
#         i = index - 1
#         current = artists [index]
#         while i >= 0:
#             if len (current) < len (artists [i]):
#                 artists [i + 1] = artists [i]
#                 artists [i] = current
#                 i -= 1
#             else: 
#                 break
    
# print (insertion_sort (artists_list))

# artists_list = [ 'Kordhell', 'DVRST', 'MC ORSEN', 'Kute', 'Green Orxnge', 'PLAYAMANE' ]

# def insertion_sort (artists):
#     for index in range (1, len (artists)):
#         i = index - 1
#         current = artists [index]
#         while i >= 0:
#             if len (current) < len (artists [i]):
#                 artists [i + 1] = artists [i]
#                 artists [i] = current
#                 i -= 1
#             else: break
    
#     return artists

# print (insertion_sort (artists_list))

# artists_list = [ 'Kordhell', 'DVRST', 'MC ORSEN', 'Kute', 'Green Orxnge', 'PLAYAMANE' ]

# def insertion_sort (artists):
#     for index in reversed (range (0, len (artists)) - 1):
#         i = index + 1
#         current = artists [index]
#         # 'current' is front of ending element in array.
#         # 'i' varable is last element.
#         while i <= len (artists) - 1:
#             if len (current) > len (artists [i]):
#                 artists [i - 1] = artists [i]
#                 artists [i] = current
#                 i += 1
#             else: break
#     return artists

# print (insertion_sort (artists_list))

# artists_list = [ 'Kordhell', 'DVRST', 'MC ORSEN', 'Kute', 'Green Orxnge', 'PLAYAMANE' ]

# def insertion_sort (artists):
#     for index in range (1, len (artists)):
#         current = artists [index]
#         i = index - 1
#         while i >= 0:
#             if len (artists [i]) > len (current):
#                 artists [i + 1] = artists [i]
#                 artists [i] = current
#                 i -= 1
#             else:
#                 break
    
#     return artists
    
# print (insertion_sort (artists_list))

artists_list = [ 'Kordhell', 'DVRST', 'MC ORSEN', 'Kute', 'Green Orxnge', 'PLAYAMANE' ]

# def insertion_sort (artists):
#     for index in range (1, len (artists)):
#         current = artists [index]
#         i = index - 1
#         while i >= 0:
#             print (artists [i])
#             i -= 1
#         print ('_________________')
#     return artists

# print (insertion_sort (artists_list))

# artists_list = [ 'Kordhell', 'DVRST', 'MC ORSEN', 'Kute', 'Green Orxnge', 'PLAYAMANE' ]
# integer = len (artists_list) - 1

# while integer >= 0:
#     print (artists_list [integer])
#     integer -= 1

# def letter_sorting (letters):
#     alphabet = [ 'a', 'b', 'c', 'd', 'i', 'f', 'g', 'y', 't' ]
#     for index in range (1, len (letters)):
#         i = index - 1
#         current = letters [index]
#         while i >= 0:
#             if alphabet.index (current) < alphabet.index (letters [i]):
#                 letters [i + 1] = letters [i]
#                 letters [i] = current
#                 i -= 1
#             else: break
    
#     return letters
    
# print (letter_sorting ([ 'y', 'b', 'c', 'd', 'i', 't', 'f' ]))

# def insertion_sort (array):
#     for index in range (1, len (array)):
#         current = array [index]
#         i = index - 1
#         while len (current) > len (array [i]):
#             array [i + 1] = array [i]
#             array [i] = current
#             if i > 0: i -= 1
#             else:
#                 break
#     return array
    
# print (insertion_sort ([ 'p', 'Ghost', 'Ride' ]))

# good ✔✔✔

# integer = 0
# songs = [ 'Deadly Heist', 'Override', 'Error! Mistake', 'Snow', 'Flare', 'Suicide Year' ]

# while integer < len (songs) - 1:
#     current = songs [integer]
#     if len (current) < len (songs [integer + 1]):
#         songs [integer] = songs [integer + 1]
#         songs [integer + 1] = current
#     integer += 1

# print (songs [-1])

# 'Kordhell', 'DVRST', 'MC ORSEN', 'Kute', 'Green Orxnge', 'PLAYAMANE'

# def insertion_sort (array):
#     for index in range (1, len (array)):
#         current = array [index]
#         while index > 0:
#             if len (array [index]) < len (array [index - 1]):
#                 array [index] = array [index - 1]
#                 array [index - 1] = current
#                 index -= 1
#             else:
#                 break
    
#     return array

# print (insertion_sort (artists_list))

# array = [ 's', 'su', 'subj', 'subject', 'sub', 'subje' ]

# for index in range (1, len (array)):
#     current = array [index]
#     while index > 0:
#         if len (current) > len (array [index - 1]):
#             array [index] = array [index - 1]
#             array [index - 1] = current
#             index -= 1
#         else:
#             break

# print (array)

# items = ['book', 'table', 'voice', 'speaking', 'advancing']
# integer = len (items) - 1

# while integer >= 0:
#     print (items [integer])
#     integer -= 1

# while integer < len (array):
#     prev = integer - 1
#     current = array [integer]
#     if len (current) < len (array [prev]):
#         array [integer] = array [prev]
#         array [prev] = current
    
#     integer += 1

# print (array)

# array = ['table', 'voice', 'advancing', 'book', 'speaking']
# integer = len (array) - 1

# while integer > 0:
#     prev = integer - 1
#     current = array [integer]
#     if (len (array [prev]) > len (current)):
#         array [integer] = array [prev]
#         array [prev] = current
#     integer -= 1

# print (array [0])

# finding lowest element, by the top to bottom

# integer = 0
# while integer < len (array) - 1:
#     current = array [integer]
#     i = integer + 1
#     Если текущий элемент больше следующего то это значит что
#     текущий элемент не самый маленький!
#     if len (current) < len (array [i]):
#         array [integer] = array [i]
#         array [i] = current
#     integer += 1

# print (array [-1])

# finding lowest element, by the bottom to top

# def lowest (array):
#     for index in range (len (array) - 1):
#         current = array [index]
#         i = index + 1
#         if len (current) > len (array [i]):
#             array [index] = array [i]
#             array [i] = current
    
#     return array [-1]

# print (lowest ([ 'After Dark', 'Close Eyes', 'milk cassette x.mp3', 'Green To Blue' ]))

# def highest (array):
#     for integer in range (len (array) - 1):
#         current = array [integer]
#         i = integer + 1
#         if len (current) < len (array [i]):
#             array [integer] = array [i]
#             array [i] = current

#     return array

# print (highest ([ 'After Dark', 'Close Eyes', 'milk cassette x.mp3', 'Green To Blue' ]))

# songs = [ 'springtail', 'snowfall', 'this feeling', 'distorted memories', 'milk cassette x.mp3', 'green to blue' ]

# def insertion_sort (songs):
#     for index in range (1, len (songs)):
#         current = songs [index]
#         while index > 0:
#             if len (current) > len (songs [index - 1]):
#                 songs [index] = songs [index - 1]
#                 songs [index - 1] = current
#                 index -= 1
#             else:
#                 break
#     return songs

# sorted_songs = insertion_sort (songs)
# print (sorted_songs)

# songs = [ 'springtail', 'snowfall', 'this feeling', 'distorted memories', 'milk cassette x.mp3', 'green to blue' ]

# def insertion_sort (array):
#     for index in range (1, len (array)):
#         i = index - 1
#         current = array [index]
#         while i >= 0:
#             if len (array [i]) > len (array [i + 1]):
#                 array [i + 1] = array [i]
#                 array [i] = current
#                 i -= 1
#             else:
#                 break
#     return array

# print (insertion_sort (songs))

# songs = [ 'springtail', 'snowfall', 'this feeling', 'distorted memories', 'milk cassette x.mp3', 'green to blue' ]

# def insertion_sort (songs):
#     for index in range (1, len (songs)):
#         current = songs [index]
#         i = index - 1
#         while i >= 0:
#             if len (songs [i]) > len (songs [i + 1]):
#                 songs [i + 1] = songs [i]
#                 songs [i] = current
#                 i -= 1
#             else:
#                 break
    
#     return songs

# print (insertion_sort (songs))

# elements = [ '*****', '......', '$$$', '~~~~~~~~~~' ]

# for index in range (len (elements)):
#     integer = 0
#     array = []
#     while integer < len (elements):
#         if len (elements [integer]) >= len (elements [index]):
#             array.append (elements [integer])
#         integer += 1
    
#     print (elements [index] +' <= ' + str (array))

# text = list ('Lorem ipsum sit amet.       qweka.........jojo')
# dotted = False
# for index in range (len (text)):
#     if text [index] == '.':
#         dotted = True
#     elif text [index] != ' ' and dotted:
#         text [index] = text [index].upper ()
#         dotted = False

# print (''.join (text))

# def insertion_sort (array):
#     for index in range (1, len (array)):
#         i = index - 1
#         current = array [index]
#         while i >= 0:
#             if len (current) < len (array [i]):
#                 array [i + 1] = array[i]
#                 array [i] = current
#                 i -= 1
#             else:
#                 break
    
#     return array

# print (insertion_sort ([ 'Flare', 'Snow', 'Judah', 'Star Way', 'Close Eyes', 'Dream Space', 'Endless Love' ]))

# array = [ 'label', 'xhori', 'violent', 'qwerty' ]

# for index in range (len (array) - 1):
#     while index >= 0:
#         current = array [index]
#         # вместо 'i' должно быть index + 1,
#         # потому что 'i' тут в цикле не меняеться
#         if len (array [index]) > len (array [index + 1]):
#             array [index] = array [index + 1]
#             array [index + 1] = current
#             index -= 1
#         else:
#             break

# print (array)

# symbols = [ '>>>>>', '......', '///', '!!!!!!!!' ]

# def sorted_symbols (symbols):
#     for index in range (len (symbols) - 1):
#         while index >= 0:
#             if len (symbols [index]) > len (symbols [index + 1]):
#                 lowerElement = symbols [index + 1]
#                 symbols [index + 1] = symbols [index]
#                 symbols [index] = lowerElement
#                 index -= 1
#             else:
#                 break
    
#     return symbols

# print (sorted_symbols (symbols))

# def duplicate_count(text):
#     result = []
#     for index in range (len (text)):
#         current = text [index]
#         integer = 0
#         while index < len (text):
#             if current == text [index]:
#                 integer += 1
#             index += 1
        
#         if integer > 1 and not (current in result):
#             result.append (current)
    
#     return len (result)

# print (duplicate_count ([ 4, 5, 4, 5, 6, 6, 6 ]))

# def duplicate_count (numbers):
#     repeat_numbers = []
#     for index in range (len (numbers)):
#         current = numbers [index]
#         integer = 0
#         while index < len (numbers):
#             if current == numbers [index]:
#                 integer += 1
#             index += 1
#         if integer > 1 and not (current in repeat_numbers):
#             repeat_numbers.append (current)
      
#     return repeat_numbers

# print (duplicate_count ([ 4, 5, 3, 2, 3, 3, 19, 48 ]))

# def duplicate_count (numbers):
#     reminder = []
#     for index in range (len (numbers)):
#         number = numbers [index]
#         try: numbers.index (number, index + 1)
#         except: pass
#         else:
#             if not (number in reminder):
#                 reminder.append (number)
#     return len (reminder)

# print (duplicate_count ([ 4, 5, 5, 4, 4, 2, 9, 48, 7 ]))

# def duplicate_count(text):
#     n = 0
#     text = text.lower()
#     for i in set(text):
#         if text.count(i) >1:
#             n += 1
#     return n

# print (duplicate_count ('abcabc'))

# def duplicate_count (word):
#     reminder = []
#     word = word.lower ()
#     for element in word:
#         if not (element in reminder) and word.count (element) > 1:
#             reminder.append (element)
#     return len (reminder)

# print (duplicate_count ('qweka'))

# Good Experienced Code ✔✔✔

# def insertion_sort (elements):
#     for index in range (len (elements)):
#         integer = len (elements) - 1
#         while integer > index:
#             current = elements [integer]
#             if elements [integer] == elements [index]:
#                 elements [integer] = elements [integer - 1]
#                 elements [integer - 1] = current
#             integer -= 1
    
#     return elements

# print (insertion_sort ([ 4, 5, 4, 3, 38, 4, 4, 19, 38, 23, 38 ]))

# BeSt PrAcTiCe 🔥

# def insertion_sort (array):
#     for index in range (len (array)):
#         integer = len (array) - 1
#         while integer > index:
#             current = array [integer]
#             if len (array [index]) == len (array [integer]):
#                 array [integer] = array [integer - 1]
#                 array [integer - 1] = current
#             integer -= 1
#     return array

# print (insertion_sort ([ 'hand', 'trash', 'basket', 'hand', 'laptop', 'audio player' ]))

# def reversed_sort (items):
#     for index in reversed (range (len (items))):
#         current = items [index]
#         integer = 0
#         while integer < index:
#             if current == items [integer]:
#                 items [integer] = items [integer + 1]
#                 items [integer + 1] = current
#             integer += 1
    
#     return items

# print (reversed_sort ([ 'hand', 'table', 'brain', 'rock', 'player', 'neuron', 'hand' ]))

# items = [ 'table', 'chair', 'flashlight', 'audio player', 'xbox', 'audio player' ]

# for index in range (len (items) - 1):
#     current = items [index]
#     if items [index] == 'audio player' and items [index + 1] != 'audio player':
#         items [index] = items [index + 1]
#         items [index + 1] = current

# print (items)
# except
# def insertion_sort (elements):
#     for index in range (len (elements)):
#         integer = len (elements) - 1
#         while integer > index:
#             current = elements [integer]
#             if elements [integer] == elements [index]:
#                 elements [integer] = elements [integer - 1]
#                 elements [integer - 1] = current
#             integer -= 1
    
#     return elements

# print (insertion_sort ([ 4, 5, 4, 3, 38, 4, 4, 19, 38, 23, 38 ]))

# def insertion_sort (elements):
#     for index in range (1, len (elements)):
#         current = elements [index]
#         i = index - 1
#         while i >= 0:
#             if current < elements [i]:
#                 elements [i + 1] = elements [i]
#                 elements [i] = current
#                 i -= 1
#             else:
#                 break
#     return elements

# print (insertion_sort ([ 4, 9, 3, 7, 5, 19, 17, 14, 19, 4, 5 ]))

# def insertion_sort (elements):
#     for index in range (len (elements)):
#         integer = len (elements) - 1
#         while integer > index:
#             current = elements [integer]
#             if elements [index] >= current:
#                 elements [integer] = elements [integer - 1]
#                 elements [integer - 1] = current
#             integer -= 1
    
#     return elements

# print (insertion_sort ([ 50, 40, 30, 20, 10]))

# def insertion_sort (elements):
#     for integer in range (1, len (elements)):
#         current = elements [integer]
#         while integer > 0:
#             if elements [integer] < elements [integer - 1]:
#                 elements [integer] = elements [integer - 1]
#                 elements [integer - 1] = current
#                 integer -= 1
#             else:
#                 break
    
#     return elements

# print (insertion_sort ([ 93, 104, 145, 56, 204, 500, 485 ]))

# def insertion_sort (arr):
#     for integer in range (1, len (arr)):
#         i = integer - 1
#         while i >= 0:
#             if arr [i] > arr [integer]:
#                 arr [i + 1] = arr [i]
#                 arr [i] = arr [integer]
#                 i -= 1
#                 continue
#             break
#     return arr

# print (insertion_sort ([ 4, 7, 8, 4, 5, 7 ]))



# def insertion_sort (elements):
#     for index in range (len (elements)):
#         integer = len (elements) - 1
#         while index < integer:
#             current = elements [integer]
#             if elements [integer] == elements [index]:
#                 elements [integer] = elements [integer - 1]
#                 elements [integer - 1] = current
#             integer -= 1
    
#     return elements

# print (insertion_sort ([ 4, 7, 8, 4, 5, 7 ]))
# def sort_emotions(arr, order):
#     return sorted(arr, key=[':D',':)',':|',':(','T_T'].index, reverse=not order)

# print (sort_emotions (['T_T', ':D', ':|', ':)'], True))

# print (sorted ([4, 0, 5, 7], key=[4, 5, 6, 7].index))
# sorted (*iterable, key=*function that takes elements of iterable object)


# array = [10, 25, 10, 40]
# filtered = sorted (array, key = [40, 25, 10].index)
# print (filtered)

# array = [4, 6, 3, 7, 9, 10, 12, 15, 14]
# sorted_elements = sorted (array, key = lambda x: x % 2 == 0)
# print (sorted_elements)

# import random

# def passwordGenerator (template):
#     result = []
#     n = len (template)
#     for i in range (n):
#         randomN = random.choice (template)
#         template.remove (randomN)
#         result.append (randomN)
#     return result

# print (passwordGenerator ([ 1, 2, 3, 4, 5 ]))

# def createDeepArray (deepness, weight, result = []):
#     deepness -= 1
#     if deepness > 0:
#         for i in range (weight):
#             result.append (createDeepArray (deepness, weight, []))
#     return result

# print (createDeepArray (2, 2))

# def findCombos (arr):
#     count = 0
#     if len (arr) == 1: return 1
#     for element in arr:
#         count += findCombos (list (filter (lambda n: n != element, arr)))
#     return count

# print (findCombos ([ 1, 2, 3 ]))


# print (list (filter (lambda n: n != 1, [1, 2, 3])))

# def cinema_seats (b, g):
#     seats = ''
#     if b > g * 2 or g > b * 2: return 'Error!'
    
#     while ( b  and  g ):
#         if b < g and not(g % b):
#             seats += 'GBG'
#             g -= 2
#             b -= 1
#             continue
#         if b > g and not(b % g):
#             seats += 'BGB'
#             b -= 2
#             g -= 1
#             continue
#         if b > g:
#             seats += 'BG'
#             b -= 1
#             g -= 1
#         else:
#             seats += 'GB'
#             b -= 1
#             g -= 1
#     return seats;

# print(cinema_seats(5, 3))


# def cinema_seats (b, g):
#     if b > g * 2: print('cool')
#     return b * 2, g * 2

# print(cinema_seats(5, 6))

# def cinema_seats (b, g):
#     if g > b * 2 or b > g * 2: return 'dhh'
    
# print(cinema_seats(11, 4))

# def cinema_seats(b, g):
#     if g > b * 2 or b > g * 2: return False

# print(cinema_seats(6, 2))

# print('qwerty' * 5)

# text = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Animi, voluptatum maxime quibusdam nemo nulla fuga eum cupiditate aspernatur dignissimos earum. Exercitationem perferendis officiis sit mollitia, perspiciatis tempora officia dolorem excepturi.'
# L = 0
# d = 0

# for symbol in text:
#     if symbol == 'L':
#         L += 1
#     elif symbol == 'd':
#         d += 1

# print(d)

# (3, 5) - gbgbggbg - correct
# (3, 6) - gbggbggbg - correct
# (3, 7) - gbggbggbg (g) - error
# (6, 3) - bgbbgbbgb - correct


# def cinema_seats (b, g):
#     result = ''
#     if b > g and g * 2 >= b:
#         for i in range(b - g): result += 'BGB'
#         for i in range(g - (b - g)): result += 'BG'
#     elif b <= g and b * 2 >= g:
#         for i in range(g - b): result += 'GBG'
#         for i in range(b - (g - b)): result += 'GB'
#     else:
#         result = 'No solves!'
#     return result

# print (cinema_seats(10, 5))

# def cinema_seats (b, g):
#     result = ''
#     if b > g * 2 or g > b * 2:
#         result = 'No solves'
#     elif b > g:
#         for i in range(b - g): result += 'BGB'
#         for i in range(g - (b - g)): result += 'BG'
#     else:
#         for i in range(g - b): result += 'GBG'
#         for i in range(b - (g - b)): result += 'GB'
#     return result
# print(cinema_seats(7, 5))

# text = 'Прив56ет, мир!!!'
# summ = 0
# arabian_numbers = '0123456789'

# for i in text:
#     if i in arabian_numbers:
#         summ += int(i)
#     else:
#         print(i, end='')

# print('\n', summ)

# bbbbbbb
# ggggg

# find the longest word

# text = 'its your life'
# longest = ''
# current = ''

# for letter in text + ' ':
#     if letter != ' ':
#         current += letter
#     else:
#         if len(longest) <= len(current):
#             longest = current
#         current = ''
# print(longest)

# text = 'mr.kitty sione the_neighbourhood arctic_monkeys MGMT'
# current = ''
# last_longest = ''

# for letter in text + ' ':
#     if letter == ' ':
#         if len(last_longest) < len(current):
#             last_longest = current
#         current = ''
#         print(last_longest)
#         continue
#     current += letter

# for word in text.split(' '):
#     if len(word) > len(last_biggest):
#         last_longest = word



# print(last_longest)
# https://youtu.be/MV_3Dpw-BRY?si=qsXv_ol11PappCFV - nightcall




# idx = 0
# for i in range(5, 11):
#     for number in range(idx, i + 1):
#         print(number, end=' ')
#     print('\n')
#     idx += 1

# for row in range(0, 6, 2):
#     for col in range(6):
#         print(row + col, end=' ')
#     print('\n')


# for i in range(0, 5, 2):
#     for g in range(1, 5):
#         print(g + i, end=' ')
#     print('\n')

# сделал таблицу сумм для чисел от 1 до 5
# к каждым числам внутри каждой новой строки
# добавляю на единицу больше чисел 
# чем в прошлый раз 

# for i in range(10):
#     for g in range(10):
#         print(i - g, end='\t')
#     print('\n')

# text = 'интересно/любопытно'

# print(text[9:10])



# text = 'slaughter'

# def slicing (txt, idx, symbol):
#     try: txt.index(symbol, idx)
#     except ValueError:
#         return txt[idx:]
#     sympl = txt.index(symbol, idx)
#     return txt[idx:sympl + 1]
    

# print(slicing(text, 1, 'g'))

# def word ():
#     return 'Hello synth world!'

# text = 'qwe qwe qwe qwe'
# boolean = True

# for idx in range(len(text)):
#     if boolean:
#         boolean = False
#     elif text[idx] == ' ':
#         boolean = True


# text = 'world sick beauty dream hardwork emptiness sadness'
# longest = sorted([ len(word) for word in text.split(' ') ])[-1]
# current = 0
# shortword = longest


# for letter in text:
#     if letter != ' ':
#         current += 1
#     else:
#         if shortword > current:
#             shortword = current
#         current = 0
# print(shortword)

# for i in range(1,4):
#     for g in range(1,6):
#         if i % 2:
#             print(g, end = ' ')
#         else:
#             print(i, end = ' ')
#     print()

# for row in range(20):
#     for col in range(50):
#         if row == 10:
#             print('-', end = '')
#         elif col == 25:
#             print('|', end = '')
#         else:
#             print(' ', end = '')
#     print()

# distance = 5
# plus = lambda x, y: x - y if x > y else y - x
# # filter

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end = '')
#         elif distance == plus(24, col):
#             if col > 24:
#                 print('\\')
#             else:
#                 print('/', end = '')
#         elif col != 24:
#             print(' ', end = '')
#         else:
#             print('|', end = '')
#     distance += 2
#     print()


# for i in range(100):
#     for i in range(4):
#         print('ofdreamthelema', end = '')
#     print()

# names = [ 'killa_blizzard', 'Redbloodyghost', 'saymyname' ]

# for iterable in names:
#     for index in range(len(names) - 1, 0, -1):
#         current = names[index]
#         names[index] = names[index - 1]
#         names[index - 1] = current
#         print(names)

#     print("\n")

# text = 'fast brown fox over the lazy dog jumped'

# def longest(txt):
#     result = ''
#     current = ''
#     for letter in txt:
#         if letter == ' ':
#             if len(result) <= len(current):
#                 result = current
#             current = ''
#         else:
#             current += letter
#     if len(result) <= len(current):
#         result = current
#     return result

# longest(text)

# numbers = [ 4, 2, 9, 12, 8, 22 ]
# result = []

# for number in numbers:
#     result.append(number)
#     index = len(result) - 1
#     while index > 0:
#         if number < result[index - 1]:
#             result[index] = result[index - 1]
#             result[index - 1] = number
#             index -= 1
#         else:
#             break
#     print(result)

# n = 3
# for i in range(n):
#     print('идет час', i)
#     for c in range(i, n):
#         print('номер в очереди', c)

# numbers = [12, 34, 2]
# prev = 1
# freq = 10
# count = 0

# for number in numbers:
#     while freq <= number:
#         num = (number % freq) // prev
#         if num == 2:
#             count += 1
#         prev *= 10
#         freq *= 10
#     num = (number % freq) // prev
#     if num == 2:
#         count += 1

# print(count)

# numbers = [ 1314, 1813, 134, 1515, 113, 131 ]
# count = 0

# for number in numbers:
#     while number > 10:
#         if number % 100 == 13:
#             count += 1
#             number //= 100
#         elif number % 100 // 10 == 3:
#             number //= 10
#         else:
#             number //= 100
#     print(count)

# numbers = [ 5511, 1144, 112, 11, 5114 ]
# result = 0

# for number in numbers:
#     while number > 0:
#         if number % 100 != 11:
#             if number % 100 // 10 == 1:
#                 number //= 10
#             else:
#                 number //= 100
#         else:
#             number //= 100
#             result += 1
#     print(result)

# numbers = [ 3, 5, 4, 2, 9 ]
# result = []

# for number in numbers:
#     count = 0
#     for devider in range(1, number):
#         if not(number % devider):
#             count += 1
#     if count == 1:
#         result.append(number)

# print(result)

# height = int(input('Укажите высоту пирамиды: '))
# final = height + height - 1

# for integer in range(1, height + 1):
#     hash_count = integer + integer - 1
#     max_count = hash_count
#     for line in range(1, final + 1):
#         if line > ( final - max_count ) // 2 and hash_count > 0:
#             print('#', end = '')
#             hash_count -= 1
#             continue
#         print(' ', end = '')
#     print()

# rows = 4
# new_num = 1
# for line in range(rows):
#     space_count = rows - line - 1
#     print('   ' * space_count, end = '')
#     for number in range(line + 1):
#         print(new_num, end = '    ')
#         new_num += 2
#     print()

# pixel graffic
# pacific ocean

# depth = int(input('Enter depth of ocean: '))

# for number in range(depth):
#     dots_count = (depth - number - 1) * 2
#     for left_nums in range(depth, depth - number - 1, -1):
#         print(left_nums, end = '')
#     print('.' * dots_count, end = '')
#     for right_nums in range(depth - number, depth + 1):
#         print(right_nums, end = '')
#     print()

# depth = 5

# for number in range(depth):
#     for left_numbers in range(depth, 0, -1):
#         if left_numbers >= depth - number:
#             print(left_numbers, end = '')
#         else:
#             print('.', end = '')
#     print()

# bet = 1234
# coefficent = 1.719
# win = 1.7999

# print('потенциальный выигрыш:', round(win, 3))

# weight = float(input('Введите вес: '))
# height = float(input('Введите рост: '))

# print(round(weight / height ** 2, 2))


# number = float(input('Введите числа с плавающейся точкой (дробные числа)'))


# print(number)

# number = 13.46

# print(round(number, 1))

# numbers = []

# for integ in range(5):
#     query_float_num = float(input('Введите дробное число: '))
#     if not(query_float_num):
#         break
#     numbers.append(query_float_num)

# for on_floated in numbers:
#     print(round(on_floated, 1))

# если число в ряду меньше 5-ти тогда оно увеличиться если число после нее больше 50 , даже 51 подходит для условии
# если число в ряду ровно или больше 5-ти то оно увеличиться если число после нее начинаеться с 5-ти

# first_number = 13.555545

# print(round(first_number, 5))


# depth = 5

# for stage in range(depth):
#     for dots in range(depth):
#         if dots <= stage:
#             print(dots + 1, end = '')
#         else:
#             print('.', end = '')
#     print()

# https://youtu.be/vmC4ENoENew?si=CHzEQEkHvAcVj22f

# stages = int(input('Enter count of stages: '))

# for stage in range(stages):
#     for line in range(stages):
#         if line <= stage:
#             print(line + 1, end = '')
#         else:
#             print('.', end = '')
#     for line in range(stages, 0, -1):
#         if line <= stage + 1:
#             print(line, end = '')
#         else:
#             print('.', end = '')
#     print()

# force = float(input('Enter Power: '))

# print(round(force, 1) * 10)

# print(
#     int(111.134)
# )

# levels = int(input('Уровень пирамиды: '))
# final_hashes = levels * 2 - 1

# for level in range(1, levels + 1):
#     current_hashes = level * 2 - 1
#     print(' ' * ( (final_hashes - current_hashes) // 2 ), end = '')
#     print('#' * current_hashes, end = '')
#     print()

# import math
# number = float(input('Введите число: '))

# print( math.ceil(number) )
# print(round(number, 7))


# levels = int(input('Укажите уровень пирамиды: '))
# start_number = 100

# for level in range(levels):
#     print('    ' * (levels - level - 1), end = '')
#     for count in range(level + 1):
#         print(start_number, end = '     ')
#         start_number += 100
#     print()

# stages = int(input('Укажите макс-ный этаж пирамиды: '))
# count = 1

# for stage in range(stages):
#     print('  ' * ( stages - stage - 1 ), end = '')
#     for line in range(stage + 1):
#         print(count, end = '  ')
#         count += 2
#     print()

# import math
# import random

# def horse_avalable(horse_pos, coord):
#     differences = 0
#     for idx in range(len(horse_pos)):
#         dif = abs(coord[idx] - horse_pos[idx])
#         if dif < 3:
#             differences += abs(coord[idx] - horse_pos[idx])
#     return differences == 3

# for attempts in range(5):
#     pos = [ 0, 0 ]
#     pos[0] = random.randint(0, 9)
#     pos[1] = random.randint(0, 9)
#     result = horse_avalable([ 2, 1 ], pos)
#     print('horse position:', [2, 1])
#     print('random position:', pos)
#     print('horse can reach there:', result)

# def triangle (line):
#     for count in range(1, line + 1):
#         star_count = count * 2 - 1
#         print(' ' * ( line - count ), end = '')
#         print(star_count * '*')
#     print()

# levels = int(input('Введите кол-во под-уровней: '))

# triangle(levels)

# height = int(input('Введите высоту пирамиды: '))

# for level in range(1, height + 1):
#     stars = (level * 2 - 1) * '*'
#     spaces = (height - level) * ' '
#     print(spaces + stars)

# level = int(input('Введите высоту пирамидки: '))
# start_number = 1

# for point in range(1, level + 1):
#     print('   ' * (level - point), end = '')
#     for integ in range(point):
#         print(start_number, end = '    ')
#         start_number += 2
#     print()

# Формула для нахождение самой большой цифры среди двух:
# (сумма первого и второго) + (модуль при отнятий от первого второго) делим на два.

# first = int(input('Введите первое число: '))
# second = int(input('Введите второе число: '))

# summa = first + second
# diferrence = abs(first - second)
# print(summa + diferrence)

# levels = int(input('Введите уровень пирамиды: '))
# final_hashes = (levels * 2) - 1

# def line_hashes (count):
#     result = ''
#     for index in range(count):
#         if not(index % 2):
#             result += '*'
#         elif index < count - 1:
#             result += ' '
#     return result

# for level in range(1, levels + 1):
#     hash_count = level * 2 - 1
#     text = line_hashes(hash_count)
#     current_lines = ' ' * (levels - level)
#     print(current_lines + text)

# import time
# for integer in range(5):
#     time.sleep(3)
#     print('Bit lox')

# print('Нет, я ошибься, Bit pedic')

# height = int(input('Введите уровень пирамиды: '))

# for point in range(height):
#     empties = ' ' * ( height - point - 1 )
#     stars = '*' * ( ( point + 1 ) * 2 - 1 )
#     print(empties + stars)


# def aboutWater (price):
#     print('Название: КлирВотер:')
#     print('Производитель: ВодЗавод')
#     if int(price) == price:
#         price = int(price)
#     print('Цена:', price)

# for count in range(3):
#     price = float(input('Введите цену воды: '))
#     aboutWater(price)

# def good():
#     print('Все хорошо.')
#     mainMenu()

# def bad():
#     print('Все плохо.')

# def mainMenu():
#     print('1. Сделать что-то хорошее')
#     print('2. Сделать что-то плохое')
#     choice = int(input('Введите номер действия: '))
#     if choice == 1:
#         good()
#     elif choice == 2:
#         bad()
#     else:
#         print('Ошибка ввода: нужно ввести 1 или 2.')


# mainMenu()

# age = int(input('Сколько вам лет? '))
# name = input('Как вас звать? ')
# gender = int(input('Каково вы пола? 0 - мужского 1 - женского '))
# marriage = 0
# suffics = [ 'к', 'ый' ]

# if not(gender):
#     gender = 'женаты'
# elif gender == 1:
#     gender = 'вышли замуж'
#     suffics = [ 'ца', 'ая' ]
# else:
#     gender = None

# if age >= 18 and gender != None:
#     que_string = 'Вы ' + gender + '? ' + '0 - нет 1 - да '
#     question = int(input(que_string))
    
#     if question == 1:
#         marriage = int(input('В каком возрасте? '))
#     elif not(question):
#         pass
#     else:
#         print('Значит нет.')

# for i in range(age + 1):
#     if not(i):
#         print('Новый человек,', name)
#     elif i == 6:
#         print('Вы теперь школьни' + suffics[0])
#     elif i == 15:
#         print('Вы теперь подросток')
#     elif i == 18:
#         print('Вы теперь взросл' + suffics[1])
#     elif i == marriage:
#         print('У вас семейная жизнь.')
#     else:
#         print(i, 'год')
# name = 'Aslan'
# def rotation (n):
#     print(name)
#     locals()
#     name = 'aslan'
#     if n > 0:
#         rotation(n - 1)

# rotation(5)


# depth = 9
# for level in range(depth):
#     for dots in range(depth):
#         if dots <= level:
#             print(dots + 1, end = '')
#         else:
#             print('.', end = '')
#     for dots in range(depth, 0, -1):
#         if dots <= level + 1:
#             print(dots, end = '')
#         else:
#             print('.', end = '')
#     print()

# def pyramids (integ, count = 1, line = 0, result = ''):
#     if count == 1: line = integ
#     for dots in range(line):
#         result += str(dots + 1) if dots < count else '.'
#     result += '\n'
#     print(result)
#     if integ > 1:
#         return pyramids(integ - 1, count + 1, line, result)
#     else:
#         return result

# print(pyramids(5))

# def rgb (red, green, blue):
#   colors = [ red, green, blue ]
#   hexcodes = '0123456789ABCDEF'
#   result = ''
#   integ = 0
#   for color in colors:
#     result += hexcodes[ color // 16 ] + hexcodes[color % 16]
#     integ += 1
#   return result

# print(rgb(255, 255, 167))

# levels = int(input('Введите нижний уровень пирамиды: '))
# number_count = 1

# for level in range(1, levels + 1):
#     for count in range(level):
#         print(number_count, end = '   ')
#         number_count += 2
#     print()


# height = int(input('Введите высоту пирамиды: '))
# 1-ый способ:
# number = 1
# for level in range(1, height + 1):
#     for line in range(level):
#         print(number, end = '   ')
#         number += 2
#     print()
# 2-ой способ:
# def pyramids(n, start = 1, start_num = 1):
#     for lines in range(start):
#         print(start_num, end = '   ')
#         start_num += 2
#     print()
#     if start < n:
#         pyramids(n, start + 1, start_num)

# pyramids(height)

# number = int(input('Введите число: '))

# def counter(number):
#     count = 0
#     while number:
#         count += 1
#         number //= 10
#     return count - 1

# def numberChange(number):
#     length = counter(number)

#     first_digit = number // 10 ** length
#     between_digits = number % 10 ** length // 10 * 10
#     last_digit = number % 10 * 10 ** length

#     return last_digit + between_digits + first_digit

# print(numberChange(number))

# def pyramid_drawer(levels):
#     levels += 1
#     for level in range(1, levels):
#         print(' ' * (levels - 1 - level), end = '')
#         print('*' * (level * 2 - 1))

# level = int(input('Введите уровень пирамиды: '))

# pyramid_drawer(level)

# def pyramid_drawer(height):
#     counter = 1
#     for integ in range(1, height + 1):
#         print('   ' * (height - integ), end = '')
#         for part in range(1, integ + 1):
#             print(counter, end = '    ')
#             counter += 2
#         print()

# level = int(input('Введите уровень пирамиды: '))
# pyramid_drawer(level)

# def pyramid_draw(levels):
#     number = 1
#     for level in range(1, levels + 1):
#         print('   ' * ( levels - level ), end = '')
#         for _ in range(level):
#             print(number, end = '    ')
#             number += 2
#         print()

# pyramid_draw(3)

# def pacific_ocean(bottom):
#     for depth in range(1, bottom + 1):
#         for line in range(bottom):
#             if line < depth:
#                 print('.', end = '')
#             else:
#                 print(' ', end = '')
#         for line in range(bottom, 0, -1):
#             if line > depth:
#                 print(' ', end = '')
#             else:
#                 print('.', end = '')
#         print()
                
# pacific_ocean(5)

# def bottom_drawer(bottom):
#     for depth in range(1, bottom + 1):
        
#         for line in range(bottom):
#             if line < depth:
#                 print(line + 1, end = '')
#             else:
#                 print('.', end = '')
#         for line in range(bottom, 0, -1):
#             if line > depth:
#                 print('.', end = '')
#             else:
#                 print(line, end = '')
#         print()
        
# bottom_drawer(6)

# INDP15PR_DRMVOYG



# image = [ ' _ _ _ ' ] + \
#         [ '|  _  |' ] + \
#         [ '| |+| |']  + \
#         [ '|_ _ _|'] 

# print('\n'.join(image))

import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
