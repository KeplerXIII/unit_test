# Тестирование приложений из домашнего задание к лекции 4, файл - homework4_app.py

import pytest
import homework4_app

FIXTURE = [
    ({'facebook': 55, 'yandex': 120, 'vk': 160, 'google': 99, 'email': 42, 'ok': 98}, "vk"),
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, "yandex"),
    ({'facebook': 160, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, "facebook")
]


@pytest.mark.parametrize("data, etalon", FIXTURE)
def test_homework_task4(data, etalon):
    result = homework4_app.task_4(data)
    assert result == etalon


FIXTURE = [
    (['2018-01-01', 'vk', 'cpc', 100], {'2018-01-01': {'vk': {'cpc': 100}}}),
    (['2018-01-01', 'mail', 'cpc', 100], {'2018-01-01': {'mail': {'cpc': 100}}}),
    (['2018-01-01', 'yandex', 'cpc', 100], {'2018-01-01': {'yandex': {'cpc': 100}}})
]


@pytest.mark.parametrize("data, etalon", FIXTURE)
def test_homework_task5(data, etalon):
    result = homework4_app.task_5(data)
    assert result == etalon

