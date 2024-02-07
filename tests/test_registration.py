from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from url_addresses import UrlAddresses


class TestRegistration:

    def test_successful_registration(self, driver_setup, user_registration):

        driver_setup.get(UrlAddresses.URL_REGISTER)
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON))
        user_email = user_registration['email']
        driver_setup.find_element(*TestLocators.REGISTRATION_INPUT_NAME).send_keys(user_registration['name'])
        driver_setup.find_element(*TestLocators.REGISTRATION_INPUT_EMAIL).send_keys(user_email)
        driver_setup.find_element(*TestLocators.REGISTRATION_INPUT_PASSWORD).send_keys(user_registration['password'])
        driver_setup.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver_setup.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(user_email)
        driver_setup.find_element(*TestLocators.LOGIN_INPUT_PASSWORD).send_keys(user_registration['password'])
        driver_setup.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))
        text_button_make_an_order = driver_setup.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER).text

        assert driver_setup.current_url == UrlAddresses.URL_MAIN_PAGE
        assert text_button_make_an_order == 'Оформить заказ'


    def test_registration_invalid_password(self, driver_setup, user_registration):

        driver_setup.get(UrlAddresses.URL_REGISTER)
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON))
        invalid_password = 'Zx12!'
        driver_setup.find_element(*TestLocators.REGISTRATION_INPUT_NAME).send_keys(user_registration['name'])
        driver_setup.find_element(*TestLocators.REGISTRATION_INPUT_EMAIL).send_keys(user_registration['email'])
        driver_setup.find_element(*TestLocators.REGISTRATION_INPUT_PASSWORD).send_keys(invalid_password)
        driver_setup.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        text_error_for_invalid_password = driver_setup.find_element(
            *TestLocators.REGISTRATION_ERROR_FOR_INVALID_PASSWORD).text

        assert text_error_for_invalid_password == 'Некорректный пароль'
