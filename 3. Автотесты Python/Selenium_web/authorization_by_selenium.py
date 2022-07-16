from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


"""Загрузка страницы с формой авторизации, её заполнение и вход в учётную запись"""

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/login')

# ожидаем пока не загрузится Username на странице
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'username')))

# поиск необходимых полей на странице для заполнения
login = driver.find_element(By.XPATH, "//input[@id='username']")
password = driver.find_element(By.XPATH, "//input[@id='password']")

# ввод логина и пароля в найденные поля
login.send_keys('admin')
password.send_keys('admin')

# поиск и нажатие кнопки Login
button_log = driver.find_element(By.XPATH, "//input[@class='btn btn-primary']")
button_log.click()

# ожидаем пока не загрузится пост на странице
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'quote')))

# html = driver.page_source  # получение html страницы
# print(html)                # выводим html в терминал

driver.quit()
