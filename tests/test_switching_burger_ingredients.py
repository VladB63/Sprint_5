from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators
from locators import PageLocators
from data import PersonData, UrlTest


# в данных проверках я учитывал поведение реального пользователя и привязал проверки
# к скрытым от пользователя элементам отображение которое в следствии клика как раз и покажет
# что переключение по разделам работает не просто отображением синей полоски под выбранным разделом и новым классом
# но и отображением контента который в себе несет выбранный раздел, прошу это учитывать
class TestSwitchingIngrediens:

    def test_switching_burger_ingredients_topping_display(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL)  # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((PageLocators.TOPPINGS_BUTTON))) # ждем готовоность кнопки перед кликом
        driver.find_element(*PageLocators.TOPPINGS_BUTTON).click() # кнопка переключения ингридиентов на начинки
        # кликаем сначала по начинкам для проверки переключения на раздел
        # что отработает скрол и покажет скрытый элемент на странице так как по умолчанию булки и соусы уже видны
        topping_in_page = driver.find_element(*PageLocators.FILLING_HEADER)
        assert topping_in_page.is_displayed()




    def test_switching_burger_ingredients_sous_display(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL)  # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((PageLocators.TOPPINGS_BUTTON))) # кликаем сначала по начинкам
        # для проверки переключения на раздел
        # что отработает скрол и покажет скрытый элемент на странице так как по умолчанию булки и соусы уже видны
        driver.find_element(*PageLocators.TOPPINGS_BUTTON).click() # кнопка переключения ингридиентов на соусы

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((PageLocators.SOUS_BUTTON)))
        driver.find_element(*PageLocators.SOUS_BUTTON).click() # а теперь кликаем на соусы потому что предыдущий клик
        # для нас скрыл данные принадлежащие разделу соусы, этим мы проверим переход из раздела в раздел

        sous_in_page = driver.find_element(*PageLocators.SOUS_HEADER)
        assert sous_in_page.is_displayed()




    def test_switching_burger_ingredients_rolls_display(self, driver):
        driver.get(UrlTest.STELLAR_URL)

        driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(PersonData.EMAIL)  # поле Email
        driver.find_element(*AuthLocators.PASS_INPUT).send_keys(PersonData.PASSWORD)  # поле пароль
        driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((PageLocators.TOPPINGS_BUTTON))) # кликаем сначала по начинкам
        # для проверки переключения на раздел
        # что отработает скрол и покажет скрытый элемент на странице так как по умолчанию булки и соусы уже видны
        driver.find_element(*PageLocators.TOPPINGS_BUTTON).click() # кнопка переключения ингридиентов на соусы

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((PageLocators.ROLLS_BUTTON)))
        driver.find_element(*PageLocators.ROLLS_BUTTON).click()  # и вот наконец то кликаем на булки потому что предыдущий
        # клик для нас скрыл данные принадлежащие разделу булки, этим мы проверим переход из раздела в раздел

        rolls_in_page = driver.find_element(*PageLocators.ROLLS_HEADER)
        assert rolls_in_page.is_displayed()


