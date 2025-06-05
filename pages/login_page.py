from selenium.webdriver.common.by import By

class LoginPageClass:
    
    def __init__(self, driver):
        self.driver=driver
        self.enter_username=(By.NAME,"user-name")
        self.enter_password=(By.CSS_SELECTOR,"#password")
        self.login_btn=(By.ID,"login-button")
        
    def launch_url(self):
        self.driver.get("https://www.saucedemo.com")
        
    def check_valid_login(self,username,password):
        self.driver.find_element(*self.enter_username).send_keys(username)
        self.driver.find_element(*self.enter_password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        
    def check_invalid_login(self,username,password):
        self.driver.find_element(*self.enter_username).send_keys(username)
        self.driver.find_element(*self.enter_password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
    
    def check_nullvalue_login(self,username,password):
        self.driver.find_element(*self.enter_username).send_keys(username)
        self.driver.find_element(*self.enter_password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        
