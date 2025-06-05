from pages.login_page import LoginPageClass

def test_valid_login(driver):
    objlogin_page=LoginPageClass(driver)
    objlogin_page.launch_url()
    objlogin_page.check_valid_login("performance_glitch_user","secret_sauce")
    objlogin_page.check_invalid_login("invalid user","wrongpwd")
    objlogin_page.check_nullvalue_login(" "," ")
    
    assert driver.title=="Swag Labs"
    print("Login Successful!!. Current url:",driver.current_url)
    