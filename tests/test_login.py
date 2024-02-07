import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from url_addresses import UrlAddresses


class TestLogin:

    @pytest.mark.parametrize('url, link_login', [
        [UrlAddresses.URL_MAIN_PAGE, TestLocators.BUTTON_SIGN_IN_TO_ACCOUNT],
        [UrlAddresses.URL_MAIN_PAGE, TestLocators.LINK_PERSONAL_AREA],
        [UrlAddresses.URL_REGISTER, TestLocators.REGISTRATION_LINK_LOGIN],
        [UrlAddresses.URL_FORGOT_PASSWORD, TestLocators.FORGOT_PASSWORD_LINK_LOGIN],
    ])
    def test_successful_login(self, url, link_login, driver_setup, login_data):

        driver_setup.get(url)
        WebDriverWait(driver_setup, 5).until(expected_conditions.element_to_be_clickable(link_login))
        driver_setup.find_element(*link_login).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver_setup.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(login_data['email'])
        driver_setup.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys(login_data['password'])
        driver_setup.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))

        assert driver_setup.current_url == UrlAddresses.URL_MAIN_PAGE
