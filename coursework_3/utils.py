import json


def load_data(filename):
    """Функция читает и возвращает данные из файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

