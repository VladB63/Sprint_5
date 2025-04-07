from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators
from locators import PageLocators
from data import PersonData, UrlTest

class TestLoginForm:

    def test_login_form_main_page(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL) # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((PageLocators.ORDER_BUTTON))) # ждем кнопку оформления заказа
        assert driver.find_element(*PageLocators.ORDER_BUTTON).text == 'Оформить заказ' # проверяем кнопку оформления заказа



    def test_login_form_in_personal_account(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*PageLocators.PERSONAL_ACCOUNT).click()  # кнопка перехода в личный кабинет
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL) # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()   # кнопка войти в аккаунт после ввода кредов
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((PageLocators.ORDER_BUTTON)))  # ждем кнопку оформления заказа
        assert driver.find_element(*PageLocators.ORDER_BUTTON).text == 'Оформить заказ' # проверяем кнопку оформления заказа




    def test_login_form_reg_form(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()    # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.REG_BUTTON_ONE).click() # кнопка перехода на форму регистрации
        driver.find_element(*AuthLocators.REG_ENTRANCE_BUTTON).click()  # кнопка войти на форме регистрации
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL) # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)    # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()    # кнопка войти в аккаунт после ввода кредов
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((PageLocators.ORDER_BUTTON))) # ждем кнопку оформления заказа
        assert driver.find_element(*PageLocators.ORDER_BUTTON).text == 'Оформить заказ' # проверяем кнопку оформления заказа




    def test_login_form_password_recovery_form(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()    # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.RECOVERY_BUTTON).click()    # кнопка восстановления пароля на форме авторизации
        driver.find_element(*AuthLocators.RECOVER_ENTRANCE_BUTTON).click()    # кнопка войти на форме восстановления пароля
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL) # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)     # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()    # кнопка войти в аккаунт после ввода кредов
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((PageLocators.ORDER_BUTTON))) # ждем кнопку оформления заказа
        assert driver.find_element(*PageLocators.ORDER_BUTTON).text == 'Оформить заказ' # проверяем кнопку оформления заказа




