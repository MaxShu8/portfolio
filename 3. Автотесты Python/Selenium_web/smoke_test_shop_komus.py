from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random


driver = webdriver.Chrome()

# Раскрываем браузер на весь экран
driver.maximize_window()

driver.get('https://www.komus.ru')

# ожидаем загрузки элемента на странице, чтобы продожить работу
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '//div[@class="b-enterAccount i-f-lt i-mr15 '
                                                                          'js-showTooltipRegion qa-choose-region gtm-cu'
                                                                          'rrent-region"]')))

# выбираем регион
choice_region = driver.find_element(By.XPATH, '//div[@class="b-enterAccount i-f-lt i-mr15 js-showTooltipRegion qa-choos'
                                              'e-region gtm-current-region"]')
choice_region.click()

confirm_region = driver.find_element(By.XPATH, '//*[@id="tippy-3"]/div[2]/div/div[2]/ul/li[3]/a')
confirm_region.click()

# ожидаем загрузки элемента на странице, чтобы продожить работу
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '//input[@class="b-search__fieldSearch siteSe'
                                                                          'archInput js-field-input qa-search-field js-'
                                                                          'search-input ui-autocomplete-input"]')))

# ищем поле ввода для поиска товара и вводим название товара
field_search = driver.find_element(By.XPATH, '//input[@class="b-search__fieldSearch siteSearchInput js-field-input qa-s'
                                             'earch-field js-search-input ui-autocomplete-input"]')
field_search.send_keys('Кофе Paulig 1 кг')

press_search_btn = driver.find_element(By.XPATH, '//input[@class="b-search__fieldSubmit qa-search-button"]')
press_search_btn.click()

WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '//input[@class="b-search__fieldSearch siteSe'
                                                                          'archInput js-field-input qa-search-field js-'
                                                                          'search-input ui-autocomplete-input"]')))

# выявляем сколько товаров по этому поисковому запросу и сохраняем число в переменную
check_value = int(driver.find_element(By.XPATH, '//span[@class="catalog__title-sup"]').text)

# рандомно выбирается любой товар из найденных
put_in_cart = driver.find_element(By.XPATH, f'//input[@from="block-123-{random.randint(1, check_value)}"]')
put_in_cart.click()

driver.implicitly_wait(5)

btn_cart = driver.find_element(By.XPATH, '//div[@class="b-cartContent mini-cart"]')
btn_cart.click()

WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '//a[@class="button button--size-l button--fu'
                                                                          'll-width button--primary js-cart-submit qa-c'
                                                                          'heckout gtm-cart-page-checkout"]')))

place_an_order = driver.find_element(By.XPATH, '//a[@class="button button--size-l button--full-width button--primary '
                                               'js-cart-submit qa-checkout gtm-cart-page-checkout"]')
place_an_order.click()

driver.quit()
