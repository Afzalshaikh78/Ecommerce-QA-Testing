from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    INVENTORY_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_TITLE)
        ).text

    def get_product_count(self):
        self.wait.until(
            EC.visibility_of_all_elements_located(self.INVENTORY_ITEMS)
        )
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(element.text.replace("$", "")) for element in elements]

    def sort_products(self, option):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        Select(dropdown).select_by_value(option)