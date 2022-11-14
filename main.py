# Домашнее задание к лекции 4. Коллекции данных.Словари. Множества.
# Выведите на экран все уникальные гео-ID из значений словаря
def task_2(location: dict) -> list:
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


# Авторизация в яндексе с ручным вводом проверочного кода, по другому как сделать не сообразил.
# По возможности прошу дать совет к реализации!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def selenium_logger(login: str, password: str) -> str:
    driver = webdriver.Chrome()
    url = "https://passport.yandex.ru/auth"
    driver.get(url)
    assert "Авторизация" in driver.title
    driver.find_element(By.CLASS_NAME, 'Button2_view_default').click()
    driver.find_element(By.ID, 'passp-field-login').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
    WebDriverWait(driver, 15).until(EC.url_changes(url))
    url = driver.current_url
    driver.find_element(By.ID, 'passp-field-passwd').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
    WebDriverWait(driver, 15).until(EC.url_changes(url))
    url = driver.current_url
    driver.find_element(By.CLASS_NAME, 'Button2_type_submit').click()
    WebDriverWait(driver, 15).until(EC.url_changes(url))
    url = driver.current_url

    return url
