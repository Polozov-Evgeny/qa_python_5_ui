import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from url_addresses import UrlAddresses


@pytest.fixture(scope='function')
def driver_setup():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user_registration():
    registration_data = {'name': 'BurgerMan',
                         'email': 'evgenii_polozov_5_' + str(random.randint(100, 999)) + '@ya.ru',
                         'password': 'Zxc12345!'}

    return registration_data


@pytest.fixture(scope='function')
def login_data():
    login_data = {'email': 'evgenii_polozov_5@ya.ru',
                  'password': 'Zxc12345!'}

    return login_data


@pytest.fixture(scope='function')
def user_login(driver_setup, login_data):

    driver_setup.get(UrlAddresses.URL_LOGIN)
    WebDriverWait(driver_setup, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
    driver_setup.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(login_data['email'])
    driver_setup.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys(login_data['password'])
    driver_setup.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver_setup, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))


@pytest.fixture(scope='class')
def driver_setup_for_class():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def user_login_for_class(driver_setup_for_class):
    login_data = {'email': 'evgenii_polozov_5@ya.ru',
                  'password': 'Zxc12345!'}

    driver_setup_for_class.get(UrlAddresses.URL_LOGIN)
    WebDriverWait(driver_setup_for_class, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
    driver_setup_for_class.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(login_data['email'])
    driver_setup_for_class.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys(login_data['password'])
    driver_setup_for_class.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver_setup_for_class, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))
