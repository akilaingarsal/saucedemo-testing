from pages.login_page import LoginPageClass
from pages.sorting_items_page import SortingItemsClass

def test_valid_login(driver):
    objlogin_page=LoginPageClass(driver)
    objlogin_page.launch_url()
    objlogin_page.check_valid_login("performance_glitch_user","secret_sauce")
    
    objSortingItems=SortingItemsClass(driver)
    
    sort_options = [
        "Name (A to Z)",
        "Name (Z to A)",
        "Price (low to high)",
        "Price (high to low)"
    ]
    
    for option in sort_options:
        objSortingItems.sort_by(option)

        if "Price" in option:
            prices = objSortingItems.get_item_prices()
            reverse_sort = "high to low" in option.lower()
            sorted_prices = sorted(prices, reverse=reverse_sort)

            print("Actual prices:", prices)
            print("Expected prices:", sorted_prices)

            assert prices == sorted_prices, f"❌ Failed on: {option} — {prices}"
            print(f"✅ Sorting verified: {option}")

        elif "Name" in option:
           
            actual_names = objSortingItems.get_item_names()
            reverse_sort = "Z to A" in option  # True if Z to A
            expected_names = sorted(actual_names, reverse=reverse_sort)

            print("Actual names:", actual_names)
            print("Expected names:", expected_names)

            assert actual_names == expected_names, f"❌ Failed on: {option} — {actual_names}"
            print(f"✅ Sorting verified: {option}")
            
    assert objSortingItems.check_products_displayed, "❌ No products displayed after login!"
print("✅ Products are displayed on the inventory page.")