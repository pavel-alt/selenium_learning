import pyautogui as pag

from random import sample, choice
from time import sleep
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

__all__ = ['open_page', 'click_on_element']

service = ChromeService(executable_path=ChromeDriverManager().install())  # устанавливаем драйвер
driver = webdriver.Chrome(service=service)  # и создаем его инстанс
driver.implicitly_wait(10)  # seconds

# driver.get(URL)  # переходим на сайт


def find_element_by_xpath(xpath_element: str) -> WebElement:
    """Поиск элемента по Х-пасу"""
    return driver.find_element(by=By.XPATH, value=xpath_element)


def find_elements_by_xpath(xpath_element: str) -> List[WebElement]:
    """Находит все элементы по Х-пасу"""
    return driver.find_elements(by=By.XPATH, value=xpath_element)


def open_page(url_page: str) -> None:
    """Открывает страницу в браузере"""
    driver.get(url_page)  # переходим на сайт


# button_change_page = driver.find_element(by=By.XPATH, value=button_change_page_xpath)  # ищем элемент для действия
# button_change_page.click()   # задаем действие для элемента
#
# sleep(5)  # TODO изучить wait


def click_on_element(xpath_element: str) -> None:
    """Клик ЛКМ по элементу"""
    element = find_element_by_xpath(xpath_element)  # ищем элемент для действия
    element.click()  # задаем действие для элемента
    # sleep(3)  # TODO изучить wait


def send_keys_by_xpath(xpath_element: str, data: str) -> None:
    """Ввод текста в поле, выбранное по Х-пасу"""
    entry_field = find_element_by_xpath(xpath_element)
    entry_field.clear()
    entry_field.send_keys(data)


def choice_el_in_dropdown_list(xpath_elements: str, target_element_xpath: str = None) -> None:
    """Выбирает вариант из выпадающего списка, найденного по Х-пасу"""
    if target_element_xpath:
        target_element = find_element_by_xpath(xpath_elements)
    else:
        all_elements = find_elements_by_xpath(xpath_elements)
        target_element = choice(all_elements)
    target_element.click()


def choice_elements_in_xpath_list(xpath_elements: str, unwanted_xpath_list: List[str] = None) -> None:
    checkboxes_accept_list = find_elements_by_xpath(xpath_elements)  # Список всех Хпасов чекбоксов на странице
    if unwanted_xpath_list:
        for xpath_el in unwanted_xpath_list:
            web_el = find_element_by_xpath(xpath_el)
            checkboxes_accept_list.remove(web_el)
    for el in sample(checkboxes_accept_list, 3):
        el.click()


def upload_file(xpath_element: str, path_2_file: str) -> None:
    """Ввод текста в поле, выбранное по Х-пасу"""
    entry_field = find_element_by_xpath(xpath_element)
    entry_field.click()
    sleep(2)
    pag.typewrite(path_2_file)
    pag.press("enter")

# for element in checkboxes_accept_list:
#     if element not in unwanted_xpath_list:
#         wanted_xpath_list.append(element)
# target_elements = sample(wanted_xpath_list, 3)
# for el in target_elements:
#     el.click()
# sleep(3)
