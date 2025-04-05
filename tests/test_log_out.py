from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators
from locators import PageLocators
from data import PersonData, UrlTest


class TestLogOut:

    def test_button_run_to_constructor_page(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL)  # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT).click() # кнопка перехода в личный кабинет
        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((PageLocators.EXIT_BUTTON)))
        driver.find_element(*PageLocators.EXIT_BUTTON).click()  # кнопка перехода в личный кабинет
        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((AuthLocators.HEADING_AUTH)))
        assert driver.find_element(*AuthLocators.AUTH_BUTTON)

