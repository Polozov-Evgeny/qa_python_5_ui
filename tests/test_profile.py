import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from url_addresses import UrlAddresses


class TestProfile:

    def test_open_profile_by_clicking_link_personal_cabinet(self, driver_setup, user_login):

        driver_setup.find_element(*TestLocators.LINK_PERSONAL_AREA).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LINK_PROFILE))

        assert driver_setup.current_url == UrlAddresses.URL_PROFILE


    @pytest.mark.parametrize('link_locator', [TestLocators.LINK_CONSTRUCTOR, TestLocators.LINK_LOGO_BURGER])
    def test_go_from_profile_to_the_constructor(self, link_locator, driver_setup, user_login):

        driver_setup.find_element(*TestLocators.LINK_PERSONAL_AREA).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LINK_PROFILE))

        driver_setup.find_element(*link_locator).click()
        WebDriverWait(driver_setup, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_AN_ORDER))

        assert driver_setup.current_url == UrlAddresses.URL_MAIN_PAGE
