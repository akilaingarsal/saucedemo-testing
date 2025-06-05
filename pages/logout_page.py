from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_btn)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
