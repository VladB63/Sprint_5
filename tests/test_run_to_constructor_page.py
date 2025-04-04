from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import AuthLocators
from locators import PageLocators


def test_button_run_to_constructor_page(email, password):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)  # поле Email
    driver.find_element(*AuthLocators.PASS_INPUT).send_keys(password)  # поле пароль
    driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов
    driver.find_element(*PageLocators.PERSONAL_ACCOUNT).click() # кнопка перехода в личный кабинет
    driver.find_element(*PageLocators.CONSTRUCTOR_BUTTON).click() # кнопка перехода в конструктор
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.find_element(By.XPATH, './/h1[text()="Соберите бургер"]')

    driver.quit()


def test_logo_run_to_constructor_page(email, password):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)  # поле Email
    driver.find_element(*AuthLocators.PASS_INPUT).send_keys(password)  # поле пароль
    driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов
    driver.find_element(*PageLocators.PERSONAL_ACCOUNT).click()  # кнопка перехода в личный кабинет
    driver.find_element(*PageLocators.LOGO_BUTTON).click()  # кнопка "конструктор" для перехода в конструктор
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.find_element(By.XPATH, './/h1[text()="Соберите бургер"]')

    driver.quit()
