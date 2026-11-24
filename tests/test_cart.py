from pages.login_page import LoginPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_and_add_product(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    return CartPage(driver)


def test_add_product_to_cart(driver):
    cart = login_and_add_product(driver)

    assert cart.get_cart_count() == 1


def test_cart_contains_correct_product(driver):
    cart = login_and_add_product(driver)
    cart.open_cart()

    assert "Sauce Labs Backpack" in cart.get_cart_product_names()


def test_remove_product_from_cart(driver):
    cart = login_and_add_product(driver)
    cart.open_cart()
    cart.remove_product()

    assert cart.get_cart_item_count() == 0


def test_continue_shopping(driver):
    cart = login_and_add_product(driver)
    cart.open_cart()
    cart.continue_shopping()

    assert "inventory.html" in driver.current_url


def test_checkout_navigation(driver):
    cart = login_and_add_product(driver)
    cart.open_cart()
    cart.click_checkout()

    WebDriverWait(driver, 10).until(
    EC.url_contains("checkout-step-one.html")
)

    assert "checkout-step-one.html" in driver.current_url