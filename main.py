# Домашнее задание к лекции 4. Коллекции данных.Словари. Множества.
# Выведите на экран все уникальные гео-ID из значений словаря
def task_2(location):
    uniq_geo = list(set(sum(list(location.values()), [])))
    return uniq_geo


# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
def task_4(stats: dict) -> str:
    best_company = max(stats, key=stats.get)
    return best_company


# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
# (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
def task_5(data_list: list) -> dict:
    if len(data_list) <= 1:
        return data_list[0]
    return {data_list[0]: task_5(data_list[1:])}


