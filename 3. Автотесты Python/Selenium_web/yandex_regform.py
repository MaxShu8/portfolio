from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://passport.yandex.ru/registration?origin=home_desktop_ru&retpath=https%3A%2F%2Fyandex.ru%2F%3Fbanerid'
           '%3D0400004260%253A61eade728433390057ff68ec%26amp%253Bclid%3D2270456%26amp%253Bwin%3D492%26ncrnd%3D176971707'
           '6&process_uuid=0ddef8a2-29dc-40e8-941e-99cfcb55423a')

field_firstname = driver.find_element(By.ID, 'firstname')
field_firstname.send_keys('Freddy')     # ввод имени в поле "Имя"

field_lastname = driver.find_element(By.ID, 'lastname')
field_lastname.send_keys('Krueger')     # ввод фамилии в поле "Фамилия"

field_login = driver.find_element(By.ID, 'login')
field_login.send_keys('freddy.krueger.ivanovich')     # ввод логина(имя почты) в поле "Придумайте логин"

field_password = driver.find_element(By.ID, 'password')
field_password.send_keys('For_Test!')     # ввод пароля в поле "Придумайте пароль"

field_password_confirm = driver.find_element(By.ID, 'password_confirm')
field_password_confirm.send_keys('For_Test!')     # ввод подтверждения пароля в поле "Повторите пароль"

field_keep_unsubscribed = driver.find_element(By.ID, 'keep_unsubscribed')
field_keep_unsubscribed.click()     # включаем чек-бокс

field_phone = driver.find_element(By.ID, 'phone')
field_phone.send_keys('800111')  # ввод номера телефона (вставить корректный номер(!))

button_phone_confirm = driver.find_element(By.CSS_SELECTOR, '#root > div > div.grid > div > main > div > div > div > fo'
                                                            'rm > div.human-confirmation-wrapper > div > div:nth-child('
                                                            '2) > div > div > button')
button_phone_confirm.click()  # нажатие на кнопку подтверждения номера телефона

driver.implicitly_wait(5)  # ожидание выполнения предыдущей операции с максимальным временем - 5 сек.

button_reg = driver.find_element(By.CSS_SELECTOR, '#root > div > div.grid > div > main > div > div > div > form > div.'
                                                  'form__submit > span > button')
button_reg.click()  # нажатие на кнопку "Зарегистрироваться"

# driver.quit()


