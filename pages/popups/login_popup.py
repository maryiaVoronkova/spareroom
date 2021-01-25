from pages.base_page import BasePage
from locators.locators import LoginPopupLocators


class LoginPopup(BasePage):

    def enter_credentials(self, email, password):
        self.driver.find_element(LoginPopupLocators.EMAIL_TEXTBOX).send_keys(email)
        self.driver.find_element(LoginPopupLocators.PASSWORD_TEXTBOX).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(LoginPopupLocators.LOGIN_BUTTON).click()
