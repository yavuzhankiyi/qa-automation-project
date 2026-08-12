from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    ITEM_NAME = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    REMOVE_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.ITEM_NAME
            )
        ).text

    def remove_item(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.REMOVE_BUTTON
            )
        ).click()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        ).click()