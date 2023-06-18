import json
import operator


def load_data(filename):
    """Функция читает и возвращает данные из файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sort_data(data):
    """Проверка по статусу и ключу date, и сортировка по нему же, возврат 5 значений"""
    sorted_data = []
    for i in data:
        if 'date' in i and i['state'] == 'EXECUTED':
            sorted_data.append(i)
    sorted_data.sort(key=operator.itemgetter('date'))
    sorted_data = sorted_data[:5]
    return sorted_data
