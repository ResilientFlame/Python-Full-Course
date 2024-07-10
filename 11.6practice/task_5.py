radius = float(input('Длинна радиуса другой планеты: '))
earth = 1.08321 * 10 ** 12
planet = 4 / 3 * 3.14 * radius ** 3

if planet > earth:
    print('другая планета больше', round(planet / earth, 3), 'раз')
else:
    print('земля больше', round(earth / planet, 3), 'раз')