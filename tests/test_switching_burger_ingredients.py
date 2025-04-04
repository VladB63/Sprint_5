from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import AuthLocators
from locators import PageLocators


# в данных проверках я учитывал поведение реального пользователя и привязал проверки
# к скрытым от пользователя элементам отображение которое в следствии клика как раз и покажет
# что переключение по разделам работает не просто отображением синей полоски под выбранным разделом и новым классом
# но и отображением контента который в себе несет выбранный раздел, прошу это учитывать
def test_switching_burger_ingredients_topping_display(email, password):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)  # поле Email
    driver.find_element(*AuthLocators.PASS_INPUT).send_keys(password)  # поле пароль
    driver.find_element(*AuthLocators.AUTH_BUTTON).click()  # кнопка войти в аккаунт после ввода кредов

    WebDriverWait(driver, 2).until(
        expected_conditions.visibility_of_element_located((PageLocators.TOPPINGS_BUTTON))) # ждем готовоность кнопки перед кликом
    driver.find_element(*PageLocators.TOPPINGS_BUTTON).click() # кнопка переключения ингридиентов на начинки
    # кликаем сначала по начинкам для проверки переключения на раздел
    # что отработает скрол и покажет скрытый элемент на странице так как по умолчанию булки и соусы уже видны
    topping_in_page = driver.find_element(By.XPATH, './/h2[text()="Начинки"]')
    assert topping_in_page.is_displayed()

    driver.quit()


def test_switching_burger_ingredients_sous_display(email, password):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)  # поле Email
    driver.find_element(*AuthLocators.PASS_INPUT).send_keys(password)  # поле пароль
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

    sous_in_page = driver.find_element(By.XPATH, './/h2[text()="Соусы"]')
    assert sous_in_page.is_displayed()

    driver.quit()


def test_switching_burger_ingredients_rolls_display(email, password):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*AuthLocators.LOG_ACCOUNT).click()  # кнопка войти в аккаунт на главной странице
    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)  # поле Email
    driver.find_element(*AuthLocators.PASS_INPUT).send_keys(password)  # поле пароль
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

    rolls_in_page = driver.find_element(By.XPATH, './/h2[text()="Булки"]')
    assert rolls_in_page.is_displayed()

    driver.quit()
