from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import RegistrationLocators


#three_number = random.randint(100, 999)
#six_number = random.randint(100000, 999999)


def test_form_registration_successful(login_random, password_6_symbol):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*RegistrationLocators.LOG_ACCOUNT).click()     # кнопка войти в аккаунт на главной странице
    driver.find_element(*RegistrationLocators.REG_BUTTON_ONE).click()  # кнопка перехода на форму регистрации
    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys('Влад') # поле имя
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(login_random) # поле Email
    driver.find_element(*RegistrationLocators.PASS_INPUT).send_keys(password_6_symbol)    # поле пароль
    driver.find_element(*RegistrationLocators.REG_BUTTON_TWO).click()    # кнопка подтверждения на форме регистрации
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((RegistrationLocators.AUTH_BUTTON)))
    assert driver.find_element(*RegistrationLocators.AUTH_BUTTON).text == 'Войти'
    driver.quit()


def test_form_registration_failed(login_random, password_3_symbol):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*RegistrationLocators.LOG_ACCOUNT).click()    # кнопка войти в аккаунт на главной странице
    driver.find_element(*RegistrationLocators.REG_BUTTON_ONE).click() # кнопка перехода на форму регистрации
    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys('Влад') # поле имя
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(login_random) # поле Email
    driver.find_element(*RegistrationLocators.PASS_INPUT).send_keys(password_3_symbol)    # поле пароль
    driver.find_element(*RegistrationLocators.REG_BUTTON_TWO).click()    # кнопка подтверждения на форме регистрации
    element = driver.find_element(By.XPATH, '//*[contains(@class, "input__error text_type_main-default")]')
    assert element.text == 'Некорректный пароль'
    driver.quit()
