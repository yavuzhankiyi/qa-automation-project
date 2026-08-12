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
        self.wait = WebDriverWait(driver, 15)

    def get_item_name(self):
        item = self.wait.until(
            EC.visibility_of_element_located(
                self.ITEM_NAME
            )
        )

        return item.text

    def remove_item(self):
        remove_button = self.wait.until(
            EC.presence_of_element_located(
                self.REMOVE_BUTTON
            )
        )

        # CI / headless ortamında daha stabil click
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            remove_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            remove_button
        )

        # Remove butonu DOM'dan kaybolana kadar bekle
        self.wait.until(
            EC.invisibility_of_element_located(
                self.REMOVE_BUTTON
            )
        )

    def is_item_present(self):
        items = self.driver.find_elements(
            *self.REMOVE_BUTTON
        )

        return len(items) > 0

    def click_checkout(self):
        self.wait.until(
            EC.url_contains(
                "cart.html"
            )
        )

        checkout_button = self.wait.until(
            EC.presence_of_element_located(
                self.CHECKOUT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            checkout_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        self.wait.until(
            EC.url_contains(
                "checkout-step-one.html"
            )
        )