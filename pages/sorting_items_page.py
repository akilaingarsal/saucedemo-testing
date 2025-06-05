from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SortingItemsClass:
    def __init__(self, driver):
        self.driver=driver
        

        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

        self.elm_item_price = (By.XPATH, "//div[@class='inventory_item_price']")

        self.elm_item_name = (By.CSS_SELECTOR, ".inventory_item_name")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")

    def sort_by(self, option_text):
        try:
            element=WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located(self.sort_dropdown)
    )
            
        except TimeoutException:
            print("Element not found within given time.")
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text(option_text)

    def get_item_prices(self):
        prices = self.driver.find_elements(*self.elm_item_price)
        return [float(price.text.replace("$", "")) for price in prices]

    def get_item_names(self):
        names = self.driver.find_elements(*self.elm_item_name)
        return [name.text for name in names]
    
    def check_products_displayed(self):
        getitems = self.driver.find_elements(*self.inventory_items)
        print("✅ Products are displayed on the page.")
        return len(getitems) > 0
        
        
