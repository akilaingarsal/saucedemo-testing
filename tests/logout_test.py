from pages.login_page import LoginPageClass
from pages.logout_page import LogoutPage
from selenium.webdriver.common.by import By
import time

def test_logout(driver):
    login = LoginPageClass(driver)
    login.launch_url()
    login.check_valid_login("performance_glitch_user", "secret_sauce")
    

    logout = LogoutPage(driver)
    logout.logout()

    assert driver.title=="Swag Labs"
    print("✅ Logout successful")
    time.sleep(2)
    
def test_invalid_login(driver):
    login = LoginPageClass(driver)
    login.launch_url()
    login.check_valid_login("incorrect_user", "pass")
    time.sleep(1)
    
    
    
    invalid_error=driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text
    assert "do not match" in invalid_error
    print("Try Again! Invalid")
    time.sleep(1)
    
def test_null_login(driver):
    login = LoginPageClass(driver)
    login.launch_url()
    login.check_nullvalue_login("","")
    
    
    null_error=driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text
    assert "required" in null_error
    print("Try Again! Username, Password required")
