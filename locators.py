from selenium.webdriver.common.by import By

class RegistrationLocators:
    LOG_ACCOUNT = By.XPATH, './/button[text()="Войти в аккаунт"]' # кнопка войти в аккаунт на главной странице
    AUTH_BUTTON = By.XPATH, './/button[text()="Войти"]' # кнопка войти в аккаунт после ввода кредов
    REG_BUTTON_ONE = By.LINK_TEXT, 'Зарегистрироваться' # кнопка перехода на форму регистрации
    NAME_INPUT = By.XPATH, './/label[text()="Имя"]/following-sibling::input[@name="name"]' # поле имя
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input[@name="name"]' # поле Email
    PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/following-sibling::input[@name="Пароль"]' # поле пароль
    REG_BUTTON_TWO = By.XPATH, './/button[text()="Зарегистрироваться"]' # кнопка подтверждения на форме регистрации
    ERROR_MESSAGE = By.XPATH, '//*[contains(@class, "input__error text_type_main-default")]'


class AuthLocators:
    LOG_ACCOUNT = By.XPATH, './/button[text()="Войти в аккаунт"]' # кнопка войти в аккаунт на главной странице
    AUTH_BUTTON = By.XPATH, './/button[text()="Войти"]' # кнопка войти в аккаунт после ввода кредов
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input[@name="name"]' # поле Email
    PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/following-sibling::input[@name="Пароль"]' # поле пароль
    REG_BUTTON_ONE = By.LINK_TEXT, 'Зарегистрироваться'  # кнопка перехода на форму регистрации
    REG_ENTRANCE_BUTTON = By.XPATH, './/a[@class="Auth_link__1fOlj"]' # кнопка войти на форме регистрации
    RECOVERY_BUTTON = By.XPATH, './/a[@href="/forgot-password"]' # кнопка восстановления пароля на форме авторизации
    RECOVER_ENTRANCE_BUTTON = By.XPATH, './/a[@href="/login"]' # кнопка войти на форме восстановления пароля
    HEADING_AUTH = By.XPATH, './/h2[text()="Вход"]'


class PageLocators:
    PERSONAL_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]'  # кнопка перехода в личный кабинет
    ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'  # кнопка оформления заказа
    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text()="Конструктор"]' # кнопка "конструктор" для перехода в конструктор
    LOGO_BUTTON = By.XPATH, './/a[@href="/"]' # кнопка Лого для перехода в конструктор
    EXIT_BUTTON = By.XPATH, './/button[text()="Выход"]' # кнопка выхода из лк
    SOUS_BUTTON = By.XPATH, './/span[text()="Соусы"]' # кнопка переключения ингридиентов на соусы
    TOPPINGS_BUTTON = By.XPATH, './/span[text()="Начинки"]' # кнопка переключения ингридиентов на начинки
    ROLLS_BUTTON = By.XPATH, './/span[text()="Булки"]' # кнопка переключения ингридиентов на булки
    HEADING_CONSTRUCTOR = By.XPATH, './/h1[text()="Соберите бургер"]' # заголовок конструктора на главной странице
    FILLING_HEADER = By.XPATH, './/h2[text()="Начинки"]'  # заголовок раздела в табличной части конструктора
    SOUS_HEADER = By.XPATH, './/h2[text()="Соусы"]'  # заголовок раздела в табличной части конструктора
    ROLLS_HEADER = By.XPATH, './/h2[text()="Булки"]'  # заголовок раздела в табличной части конструктора
    PROFILE_LINK = By.XPATH, '//a[@href="/account/profile"]' # текстовая кнопка "Профиль" в личном кабинете

