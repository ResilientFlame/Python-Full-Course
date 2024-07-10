import math

pocket_size = float(input('Укажите размер файла для скачивания: '))
internet_speed = float(input('Какова скорость вашего соединения: '))
seconds = 1
downloaded = internet_speed

while downloaded < pocket_size:
    percents = math.floor(downloaded * 100 / pocket_size)
    print('Прошло', seconds, 'сек.', 'Скачано',round(downloaded,1), 'из', pocket_size, 'Мб', '(', percents,'%)')
    downloaded += internet_speed
    seconds += 1
else:
    downloaded = pocket_size
    percents = math.floor(downloaded * 100 / pocket_size)
    print('Прошло', seconds, 'сек.', 'Скачано', math.floor(downloaded), 'из', pocket_size, 'Мб', '(', percents,'%)')