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


def prepare_data(data):
    """Подготовка данных для отображения"""
    output = ''
    for i in data:
        output += f"{i['date'][8:10]}.{i['date'][5:7]}.{i['date'][:4]} {i['description']} \n"
        to = i['to'].split()
        try:
            from_ = i['from'].split()
            for x in from_:
                if x.isalpha():
                    output += f"{x} "
                else:
                    if len(x) == 16:
                        output += f"{x[:4]} {x[4:6]}** **** {x[:4]} -> "
                    else:
                        output += f"**{x[:4]} -> "
        except KeyError:
            pass
        for y in to:
            if y.isalpha():
                output += f"{y} "
            else:
                if len(y) == 16:
                    output += f"{y[:4]} {y[4:6]}** **** {y[:4]} \n"
                else:
                    output += f"**{y[:4]} \n"
        output += f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']} \n"
        output += '\n'
    return output
