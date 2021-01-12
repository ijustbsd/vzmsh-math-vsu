import csv

INPUT_CSV = 'data.csv'
OUTPUT_CSV = 'pelican/participants.csv'


def str_formatter(x):
    extra = {
        'нет': '-',
        '': '-',
        ' ': '-',
        'без доклада': '-'
    }
    # делаем замены некоторых строк фиксированными значениями
    if x in extra:
        return extra[x]
    # меняем двойные пробелы на одинарные
    x = x.replace('  ', ' ')
    # если строка записана на 2-х языках через "/", то удаляем 2-ой язык
    x = x.split('/')[0]
    # если строка заканчивается пробелом, то удаляем его
    x = x[:-1] if x[-1] == ' ' else x
    return x


result = []
with open(INPUT_CSV) as csvfile:
    reader = csv.reader(csvfile)
    # скипаем заголовки столбцов
    next(reader)
    for row in reader:
        # фамилия, имя, отчество, город, тема доклада
        result.append([row[1], row[2], row[3], row[4], row[11]])
# форматируем каждый столбец в строке
result = [tuple(map(str_formatter, x)) for x in result]
# убираем дубликаты
result = set(result)
# сортируем по алфавиту, учитывая ФИО и тему
result = sorted(result, key=lambda x: ''.join(x))

# сохраняем обработанные данные
with open(OUTPUT_CSV, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for x in result:
        writer.writerow(x)
