import random
from time import sleep

from pyautogui import press
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Мы скачиваем драйверы для Хрома

service = ChromeService(executable_path=ChromeDriverManager().install())  # устанавливаем драйвер
driver = webdriver.Chrome(service=service)  # и создаем его инстанс
driver.implicitly_wait(10)  # задержка до исполнения (seconds)

url_page = 'https://2048game.com/ru'  # Указали адрес

driver.get(url_page)  # переходим на сайт
sleep(3)

button_new_game_xpath = '//div[2]/a'

button_element = driver.find_element(by=By.XPATH, value=button_new_game_xpath)
button_element.click()

direction_list = ['down', 'up', 'left', 'right']

button_try_again_xpath = '//div[@class="game-message"]/p'
button_try_again = driver.find_element(by=By.XPATH, value=button_try_again_xpath)

while not button_try_again.text:
    sleep(0.5)
    press(random.choice(direction_list))


