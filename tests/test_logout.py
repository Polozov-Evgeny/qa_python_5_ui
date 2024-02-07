from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from url_addresses import UrlAddresses


class TestLogout:

    def test_successful_logout(self, driver_setup, user_login):

        driver_setup.find_element(*TestLocators.LINK_PERSONAL_AREA).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

        driver_setup.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        assert driver_setup.current_url == UrlAddresses.URL_LOGIN
