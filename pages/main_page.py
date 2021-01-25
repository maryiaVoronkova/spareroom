from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):

    def click_login_button(self):
        self.driver.find_element(MainPageLocators.LOGIN_BUTTON).click()

    def click_search(self):
        self.driver.find_element(MainPageLocators.SEARCH_MENU_ITEM).click()
