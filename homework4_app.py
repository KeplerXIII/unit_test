from pprint import pprint


def task_1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    check_country = "Россия"

    result_list = []
    for visit in geo_logs:
        if check_country in list(visit.values())[0]:
            result_list.append(visit)
    pprint(result_list)


def task_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    uniq_geo = list(set(sum(list(ids.values()), [])))
    print(uniq_geo)


def task_3():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]

    result = {}
    avg_requests = len(queries)
    for request in queries:
        result.setdefault(len(request.split()), 0)
        result[len(request.split())] += 1
    for request_dict in result:
        pprint(f'Запросов состоящих из {request_dict} слов - {round(result[request_dict] / avg_requests * 100, 2)}%')


def task_4(stats: dict) -> str:
    best_company = max(stats, key=stats.get)
    return best_company


def task_5(data_list):
    if len(data_list) <= 1:
        return data_list[0]
    return {data_list[0]: task_5(data_list[1:])}
