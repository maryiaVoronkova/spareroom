import json
from driver import Driver

from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.popups.login_popup import LoginPopup
from data.test_data import *


driver = Driver(URL)
main_page = MainPage(driver)
login_popup = LoginPopup(driver)
search_page = SearchPage(driver)


def get_credentials():
    with open("data/users.json") as data_file:
        users = json.load(data_file)
    user = users["users"][0]
    return user["email"], user["password"]


def login_to_source(user_email, user_password):
    main_page.click_login_button()
    login_popup.enter_credentials(user_email, user_password)
    login_popup.click_login_button()


def search_rooms_by_location_and_max_price(location, max_price):
    main_page.click_search()
    search_page.open_advanced_search()
    search_page.enter_location(location)
    search_page.enter_max_rent(max_price)
    search_page.click_search_button()


def quit_driver():
    driver.quit()


if __name__ == '__main__':
    email, password = get_credentials()
    login_to_source(email, password)
    search_rooms_by_location_and_max_price(LOCATION, MAX_RENT)
    quit_driver()
