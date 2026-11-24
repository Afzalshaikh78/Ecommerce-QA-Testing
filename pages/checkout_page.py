from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    CANCEL = (By.ID, "cancel")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    SUMMARY_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_customer_details(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(
            self.FIRST_NAME)).send_keys(first)

        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)

    def continue_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE)
        ).click()

    def get_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR)
        ).text

    def get_item_count(self):
        return len(self.driver.find_elements(*self.SUMMARY_ITEMS))

    def get_total_text(self, locator):
        return self.driver.find_element(*locator).text

    def finish_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH)
        ).click()

    def get_confirmation(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text

    def return_home(self):
        self.driver.find_element(*self.BACK_HOME).click()