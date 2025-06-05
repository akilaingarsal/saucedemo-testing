from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPageClass:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_btn = (By.ID, "checkout")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def go_to_cart(self):
        try:
            cart_btn=WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.cart_icon))
            
            print("products added to cart")
            cart_btn.click()
        
    
            
        except TimeoutException:
            print("Element not found within given time.")
    
    def click_checkout(self):
        try:
            checkoutbtn=WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.checkout_btn))
            checkoutbtn.click()
        except TimeoutException:
            print("Element not found within given time.")

    def fill_checkout_info(self, fname="Akila", lname="QA", zip="636705"):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.zip_code).send_keys(zip)
        self.driver.find_element(*self.continue_btn).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()

    def get_subtotal(self):
        text = self.driver.find_element(*self.subtotal_label).text
        print("got subtotal")
        return float(text.split("$")[1])

    def get_total(self):
        text = self.driver.find_element(*self.total_label).text
        print("got total")
        return float(text.split("$")[1])