from selenium.webdriver.common.by import By


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

    def get_item_name(self):
        return self.driver.find_element(
            *self.ITEM_NAME
        ).text

    def remove_item(self):
        self.driver.find_element(
            *self.REMOVE_BUTTON
        ).click()

    def click_checkout(self):
        self.driver.find_element(
            *self.CHECKOUT_BUTTON
        ).click()