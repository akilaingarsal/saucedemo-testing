from pages.login_page import LoginPageClass
from pages.cart_validate_page import CartPageClass

from selenium.webdriver.common.by import By

def test_valid_login(driver):
    objlogin_page=LoginPageClass(driver)
    objlogin_page.launch_url()
    objlogin_page.check_valid_login("performance_glitch_user","secret_sauce")


   
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[1].click()

    objcart = CartPageClass(driver)
    objcart.go_to_cart()
    objcart.click_checkout()
    objcart.fill_checkout_info()

    subtotal = objcart.get_subtotal()
    total = objcart.get_total()

    
    assert total >= subtotal, "❌ Total should be greater than or equal to subtotal"
    print(f"✅ Subtotal: ${subtotal}, Total: ${total}")

    objcart.click_finish()
