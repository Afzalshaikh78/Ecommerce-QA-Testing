from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def get_cart_product_names(self):
        elements = self.driver.find_elements(*self.CART_PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BUTTONS)
        ).click()

    def continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        ).click()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()