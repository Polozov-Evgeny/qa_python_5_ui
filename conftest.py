import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from url_addresses import UrlAddresses
from test_data import TestData


@pytest.fixture(scope='function')
def driver_setup():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user_login(driver_setup):

    driver_setup.get(UrlAddresses.URL_LOGIN)
    WebDriverWait(driver_setup, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
    driver_setup.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(TestData.LOGIN_DATA['email'])
    driver_setup.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys(TestData.LOGIN_DATA['password'])
    driver_setup.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver_setup, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))
