from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.ID, "show-user-auth-popup")
    SEARCH_MENU_ITEM = (By.XPATH, "//a[contains(@class, 'nav-bar__link--search')]")


class LoginPopupLocators:
    EMAIL_TEXTBOX = (By.ID, "loginemail")
    PASSWORD_TEXTBOX = (By.ID, "loginpass")
    LOGIN_BUTTON = (By.ID, "sign-in-button")


class SearchPageLocators:
    ADVANCED_SEARCH_TAB = (By.XPATH, "//*[@class='panel-tab']//a[.='Advanced Search']")
    LOCATION_TEXTBOX = (By.ID, "search_by_location_field")
    MAX_RENT_INPUT = (By.XPATH, "//input[@name='max_rent']")
    SEARCH_BUTTON = (By.ID, "search-button")
