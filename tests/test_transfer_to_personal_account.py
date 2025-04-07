from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators
from locators import PageLocators
from data import PersonData, UrlTest


class TestTransferPersonAcc:

    def test_button_transfer_to_personal_acc(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL)  # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT).click() # кнопка перехода в личный кабинет
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((PageLocators.PROFILE_LINK)))
        assert driver.find_element(*PageLocators.PROFILE_LINK)



