
import pytest
from pages.login_page import LoginPage
import json
from utilities.logger import logger

with open("test_data/login_data.json", "r") as file:
    login_data = json.load(file)


test_data = [
    (item["username"], item["password"], item["expected_error"])
    for item in login_data
]

@pytest.mark.parametrize(
    "username,password,expected_error",
    test_data
)

def test_invalid_login(driver, username, password, expected_error):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(username, password)

    actual_error = login_page.get_error_message()

    assert expected_error in actual_error


def test_valid_login(driver):
    logger.info("Starting valid login test")

    login_page = LoginPage(driver)
    login_page.open()

    logger.info("Entering valid credentials")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    logger.info("Valid login test passed")