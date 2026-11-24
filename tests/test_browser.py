
def test_browser(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"