from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver:

    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    def find_element(self, locator, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator),
                                                      message=f"Element with locator {locator} is not present")

    def quit(self):
        self.driver.quit()
