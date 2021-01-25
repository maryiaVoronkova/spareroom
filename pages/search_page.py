from pages.base_page import BasePage
from locators.locators import SearchPageLocators


class SearchPage(BasePage):

    def open_advanced_search(self):
        self.driver.find_element(SearchPageLocators.ADVANCED_SEARCH_TAB).click()

    def enter_location(self, location):
        self.driver.find_element(SearchPageLocators.LOCATION_TEXTBOX).send_keys(location)

    def enter_max_rent(self, rent):
        self.driver.find_element(SearchPageLocators.MAX_RENT_INPUT).send_keys(rent)

    def click_search_button(self):
        self.driver.find_element(SearchPageLocators.SEARCH_BUTTON).click()
