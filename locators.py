from selenium.webdriver.common.by import By


class TestLocators:

    # Страница регистрации
    REGISTRATION_INPUT_NAME = By.XPATH, ".//label[text() = 'Имя']/parent::div/input"
    REGISTRATION_INPUT_EMAIL = By.XPATH, ".//label[text() = 'Email']/parent::div/input"
    REGISTRATION_INPUT_PASSWORD = By.XPATH, ".//input[@name = 'Пароль']"
    REGISTRATION_BUTTON = By.XPATH, ".//button[text() = 'Зарегистрироваться']"
    REGISTRATION_ERROR_FOR_INVALID_PASSWORD = By.CLASS_NAME, "input__error"
    REGISTRATION_LINK_LOGIN = By.XPATH, ".//a[@href = '/login']"

    # Страница авторизации
    LOGIN_INPUT_EMAIL = By.XPATH, ".//label[text() = 'Email']/parent::div/input"
    LOGIN_INPUT_PASSWORD = By.XPATH, ".//input[@name = 'Пароль']"
    LOGIN_BUTTON = By.XPATH, ".//button[text() = 'Войти']"

    # Страница восстановления пароля
    FORGOT_PASSWORD_LINK_LOGIN = By.XPATH, ".//a[@href = '/login']"

    # Главная страница / Конструктор
    BUTTON_MAKE_AN_ORDER = By.XPATH, ".//button[text() = 'Оформить заказ']"
    BUTTON_SIGN_IN_TO_ACCOUNT = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    LINK_PERSONAL_AREA = By.XPATH, ".//p[text() = 'Личный Кабинет']"
    LINK_CONSTRUCTOR = By.XPATH, ".//p[text() = 'Конструктор']"
    LINK_LOGO_BURGER = By.XPATH, '//nav/div/a'
    TAB_BUNS = By.XPATH, ".//span[text() = 'Булки']/parent::div"
    TAB_SOUSES = By.XPATH, ".//span[text() = 'Соусы']/parent::div"
    TAB_INGREDIENTS = By.XPATH, ".//span[text() = 'Начинки']/parent::div"

    # Личный кабинет
    LINK_PROFILE = By.XPATH, ".//a[@href = '/account/profile']"
    LOGOUT_BUTTON = By.XPATH, ".//button[text() = 'Выход']"
