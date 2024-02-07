import pytest

from locators import TestLocators


class TestConstructor:

    @pytest.mark.parametrize('link_tab', [
        TestLocators.TAB_SOUSES,
        TestLocators.TAB_INGREDIENTS,
        TestLocators.TAB_BUNS
    ])
    def test_tab_switching(self, link_tab, driver_setup_for_class, user_login_for_class):

        tab_element = driver_setup_for_class.find_element(*link_tab)
        tab_element.click()
        result_class = tab_element.get_attribute('class')

        assert 'current' in result_class
