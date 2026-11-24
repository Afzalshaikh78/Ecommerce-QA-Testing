from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_and_open_inventory(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return InventoryPage(driver)


def test_inventory_page_loads(driver):
    inventory = login_and_open_inventory(driver)

    assert inventory.get_page_title() == "Products"


def test_product_count(driver):
    inventory = login_and_open_inventory(driver)

    assert inventory.get_product_count() == 6


def test_product_names(driver):
    inventory = login_and_open_inventory(driver)

    names = inventory.get_product_names()

    assert len(names) == 6
    assert all(names)


def test_product_prices(driver):
    inventory = login_and_open_inventory(driver)

    prices = inventory.get_product_prices()

    assert len(prices) == 6
    assert all(price > 0 for price in prices)


def test_sort_products_az(driver):
    inventory = login_and_open_inventory(driver)

    inventory.sort_products("az")
    names = inventory.get_product_names()

    assert names == sorted(names)


def test_sort_products_za(driver):
    inventory = login_and_open_inventory(driver)

    inventory.sort_products("za")
    names = inventory.get_product_names()

    assert names == sorted(names, reverse=True)


def test_sort_products_low_to_high(driver):
    inventory = login_and_open_inventory(driver)

    inventory.sort_products("lohi")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices)


def test_sort_products_high_to_low(driver):
    inventory = login_and_open_inventory(driver)

    inventory.sort_products("hilo")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices, reverse=True)