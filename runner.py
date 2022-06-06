from random import sample

from my_framework import open_page, click_on_element, send_keys_by_xpath, choice_el_in_dropdown_list, \
    find_elements_by_xpath, find_element_by_xpath, choice_elements_in_xpath_list, upload_file
from urls import URL_HOME

open_page(URL_HOME)

button_change_page_xpath = './/a[contains(@class, "start")]'  # пишем руками Хпас
click_on_element(button_change_page_xpath)


password_field_xpath = '/html/body/div/div/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[2]/input'
password = 'Aд34567890'
send_keys_by_xpath(password_field_xpath, password)

mail_field_xpath = '/html/body/div/div/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[1]/input'
mail = 'Aaa'
send_keys_by_xpath(mail_field_xpath, mail)

domain_field_xpath = '/html/body/div/div/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[3]/input'
domain = 'gmail'
send_keys_by_xpath(domain_field_xpath, domain)

choice_of_first_order_domain_xpath = ".//div[@class='dropdown__list-item']"
dropdown_opener_xpath = ".//div[@class='dropdown__opener']"
click_on_element(dropdown_opener_xpath)
choice_el_in_dropdown_list(choice_of_first_order_domain_xpath)

checkbox_accept_xpath = './/span[contains(@class, "checkbox__check")]'  # пишем руками Хпас
click_on_element(checkbox_accept_xpath)

button_next_xpath = './/a[text()="Next"]'   # пишем руками Хпас
click_on_element(button_next_xpath)

checkboxes_accept_xpath = 'c'  # все Хпасы чекбоксов на странице
checkbox_unselect_all_xpath = './/label[@for="interest_unselectall" ]/span'  # Хпас чекбокса unselect_all

click_on_element(checkbox_unselect_all_xpath)   # клик на анселект_алл и снимаем все выделенные чекбоксы
unwanted_xpath_list = ['.//span[contains(@class, "checkbox__box")]', './/label[@for="interest_selectall" ]/span']
choice_elements_in_xpath_list(checkboxes_accept_xpath, unwanted_xpath_list)

upload_img_button_xpath = './/a[@class="avatar-and-interests__upload-button"]'
path_2_file = fr'C:\1.jpg'

upload_file(upload_img_button_xpath, path_2_file)

button_next_2_xpath = './/button[text()="Next"]'
click_on_element(button_next_2_xpath)

# password_entry_field = driver.find_element(by=By.XPATH, value=password_entry_field_xpath)
# password_entry_field.clear()
# password_entry_field.send_keys('Aд34567890')
# sleep(5)
#
# mail_field_xpath = '/html/body/div/div/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[1]/input'
# mail_entry_field = driver.find_element(by=By.XPATH, value=mail_entry_field_xpath)
# mail_entry_field.clear()
# mail_entry_field.send_keys('Aaa')
# sleep(5)
#
# domain_entry_field_xpath = '/html/body/div/div/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[3]/input'
# domain_entry_field = driver.find_element(by=By.XPATH, value=domain_entry_field_xpath)
# domain_entry_field.clear()
# domain_entry_field.send_keys('gmail')
# sleep(5)


