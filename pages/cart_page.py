from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

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

    def get_item_name(self):
        return self.get_text(
            self.ITEM_NAME
        )

    def remove_item(self):
        self.js_click(
            self.REMOVE_BUTTON
        )

        self.wait_until_invisible(
            self.REMOVE_BUTTON
        )

    def is_item_present(self):
        return self.is_present(
            self.REMOVE_BUTTON
        )

    def click_checkout(self):
        self.wait_for_url(
            "cart.html"
        )

        self.js_click(
            self.CHECKOUT_BUTTON
        )

        self.wait_for_url(
            "checkout-step-one.html"
        )
