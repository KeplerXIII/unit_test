from user import YA_TOKEN
import ya_api
import pytest
import main

# Тестирование приложений из домашнего задание к лекции 4
# Тестирование решения 2 задания
FIXTURE = [
    ({'user1': [213, 213, 213, 15, 213], 'user2': [57, 57, 119, 119, 119], 'user3': [213, 98, 98, 35]},
     [98, 35, 15, 213, 119, 57]),
    ({'user1': [213, 213, 213, 25, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]},
     [98, 35, 213, 54, 119, 25]),
    ({'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]},
     [98, 35, 15, 213, 54, 119])
]


@pytest.mark.parametrize("data, etalon", FIXTURE)
def test_homework_task2(data, etalon):
    result = main.task_2(data)
    assert result == etalon


# Тестирование решения 4 задания
FIXTURE = [
    ({'facebook': 55, 'yandex': 120, 'vk': 160, 'google': 99, 'email': 42, 'ok': 98}, "vk"),
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, "yandex"),
    ({'facebook': 160, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, "facebook")
]


@pytest.mark.parametrize("data, etalon", FIXTURE)
def test_homework_task4(data, etalon):
    result = main.task_4(data)
    assert result == etalon


# Тестирование решения 5 задания
FIXTURE = [
    (['2018-01-01', 'vk', 'cpc', 100], {'2018-01-01': {'vk': {'cpc': 100}}}),
    (['2018-01-01', 'mail', 'cpc', 100], {'2018-01-01': {'mail': {'cpc': 100}}}),
    (['2018-01-01', 'yandex', 'cpc', 100], {'2018-01-01': {'yandex': {'cpc': 100}}})
]


@pytest.mark.parametrize("data, etalon", FIXTURE)
def test_homework_task5(data, etalon):
    result = main.task_5(data)
    assert result == etalon


# Тестирование функции создания папки на Яндекс диске
FIXTURE = [
    ('1'),
    ('2'),
    ('3')
]


@pytest.mark.parametrize("data", FIXTURE)
def test_ya_api_creation_folder(data):
    ya = ya_api.YandexDisk(token=YA_TOKEN)
    result = ya.create_folder(data)
    assert result == 201 or result == 409
    result = ya.delete_folder(data)
    assert result == 204


# Тестирование авторизации.
from user import my_login, my_password
from main import selenium_logger

FIXTURE = [
    (my_login, my_password)
]


@pytest.mark.parametrize("login, password", FIXTURE)
def test_ya_selenium_logger(login, password):
    result = selenium_logger(login, password)
    personal_cabinet = "https://id.yandex.ru/"
    assert result == personal_cabinet
