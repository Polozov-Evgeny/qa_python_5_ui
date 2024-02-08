from locators import TestLocators


class TestConstructor:

    def test_switch_buns_tab(self, driver_setup, user_login):

        driver_setup.find_element(*TestLocators.TAB_SOUSES).click()
        tab_element = driver_setup.find_element(*TestLocators.TAB_BUNS)
        tab_element.click()
        result_class = tab_element.get_attribute('class')

        assert 'current' in result_class

    def test_switch_souses_tab(self, driver_setup, user_login):

        tab_element = driver_setup.find_element(*TestLocators.TAB_SOUSES)
        tab_element.click()
        result_class = tab_element.get_attribute('class')

        assert 'current' in result_class

    def test_switch_ingredients_tab(self, driver_setup, user_login):

        tab_element = driver_setup.find_element(*TestLocators.TAB_INGREDIENTS)
        tab_element.click()
        result_class = tab_element.get_attribute('class')

        assert 'current' in result_class
