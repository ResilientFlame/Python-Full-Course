start_amplitude = float(input('Введите начальную амплитуду: '))
end_amplitude = float(input('Введите амплитуду остановки: '))
count = 0

while start_amplitude > end_amplitude:
    start_amplitude = start_amplitude * 91.6 / 100
    count += 1

print('Маятник считается остановившимся через', count, 'колебаний.')