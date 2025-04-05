from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators
from locators import PageLocators
from data import PersonData, UrlTest

class TestRunConstructor:

    def test_button_run_to_constructor_page(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL)  # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT).click() # кнопка перехода в личный кабинет
        driver.find_element(*PageLocators.CONSTRUCTOR_BUTTON).click() # кнопка перехода в конструктор
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((PageLocators.HEADING_CONSTRUCTOR)))
        assert driver.find_element(*PageLocators.HEADING_CONSTRUCTOR)




    def test_logo_run_to_constructor_page(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL)  # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT).click()  # кнопка перехода в личный кабинет
        driver.find_element(*PageLocators.LOGO_BUTTON).click()  # кнопка "конструктор" для перехода в конструктор
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((PageLocators.HEADING_CONSTRUCTOR)))
        assert driver.find_element(*PageLocators.HEADING_CONSTRUCTOR)


