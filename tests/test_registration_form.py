from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationLocators
from helpers import login_random, password_6_symbol, password_3_symbol
from data import UrlTest


class TestRegForm:

    def test_form_registration_successful(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*RegistrationLocators.LOG_ACCOUNT).click()     # кнопка войти в аккаунт на главной странице
        driver.find_element(*RegistrationLocators.REG_BUTTON_ONE).click()  # кнопка перехода на форму регистрации
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys('Влад') # поле имя
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(login_random()) # поле Email
        driver.find_element(*RegistrationLocators.PASS_INPUT).send_keys(password_6_symbol())    # поле пароль
        driver.find_element(*RegistrationLocators.REG_BUTTON_TWO).click()    # кнопка подтверждения на форме регистрации
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((RegistrationLocators.AUTH_BUTTON)))
        assert driver.find_element(*RegistrationLocators.AUTH_BUTTON).text == 'Войти'



    def test_form_registration_failed(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*RegistrationLocators.LOG_ACCOUNT).click()    # кнопка войти в аккаунт на главной странице
        driver.find_element(*RegistrationLocators.REG_BUTTON_ONE).click() # кнопка перехода на форму регистрации
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys('Влад') # поле имя
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(login_random()) # поле Email
        driver.find_element(*RegistrationLocators.PASS_INPUT).send_keys(password_3_symbol())    # поле пароль
        driver.find_element(*RegistrationLocators.REG_BUTTON_TWO).click()    # кнопка подтверждения на форме регистрации
        element = driver.find_element(*RegistrationLocators.ERROR_MESSAGE)
        assert element.text == 'Некорректный пароль'

