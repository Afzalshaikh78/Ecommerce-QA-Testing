import pytest

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    cart = CartPage(driver)
    cart.open_cart()
    cart.click_checkout()

    return CheckoutPage(driver)


def test_checkout_empty_fields(driver):
    checkout = open_checkout(driver)
    checkout.continue_checkout()

    assert "First Name is required" in checkout.get_error()


def test_checkout_missing_last_name(driver):
    checkout = open_checkout(driver)
    checkout.enter_customer_details("Afzal", "", "400001")
    checkout.continue_checkout()

    assert "Last Name is required" in checkout.get_error()


def test_checkout_missing_postal_code(driver):
    checkout = open_checkout(driver)
    checkout.enter_customer_details("Afzal", "Shaikh", "")
    checkout.continue_checkout()

    assert "Postal Code is required" in checkout.get_error()


def test_checkout_order_summary(driver):
    checkout = open_checkout(driver)
    checkout.enter_customer_details("Afzal", "Shaikh", "400001")
    checkout.continue_checkout()

    assert checkout.get_item_count() == 1

    item_total = checkout.get_total_text(checkout.ITEM_TOTAL)
    tax = checkout.get_total_text(checkout.TAX)
    total = checkout.get_total_text(checkout.TOTAL)

    assert item_total.startswith("Item total:")
    assert tax.startswith("Tax:")
    assert total.startswith("Total:")


def test_successful_order(driver):
    checkout = open_checkout(driver)

    checkout.enter_customer_details("Afzal", "Shaikh", "400001")
    checkout.continue_checkout()
    checkout.finish_order()

    assert checkout.get_confirmation() == "Thank you for your order!"



def test_empty_cart_checkout_defect(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.open_cart()
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.continue_checkout()

    # Empty cart should not allow order completion.
    assert checkout.get_item_count() > 0