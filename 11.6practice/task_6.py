import math

print('Введите местоположение коня:')
horse_x = int(float(input('по горизонтали: ')) * 10)
horse_y = int(float(input('по вертикали: ')) * 10)
print('Введите местоположение точки на доске:')
loc_x = int(float(input('по горизонтали: ')) * 10)
loc_y = int(float(input('по вертикали: ')) * 10)

print('Конь в клетке(', horse_x,',', horse_y,')', end = '. ')
print('Точка в клетке(', loc_x,',', loc_y,').' )

cube_count = 3

differences = 0
if abs(loc_x - horse_x) < 3:
    differences = abs(loc_x - horse_x) + abs(loc_y - horse_y)

if differences == 3:
    print('Да, конь может ходить в эту точку.')
else:
    print('Конь не может туда дойти')

# Конь в клетке (0, 1). Точка в клетке (2, 0)
# Конь в клетке (0, 1). Точка в клетке (2, 0)
# Конь в клетке (0, 1). Точка в клетке (2, 0)
# Конь в клетке (0, 1). Точка в клетке (2, 0)