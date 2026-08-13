from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.config import BASE_URL


class ProductsPage(BasePage):

    ADD_BACKPACK_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    SORT_DROPDOWN = (
        By.CLASS_NAME,
        "product_sort_container"
    )

    PRODUCT_PRICES = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    def add_backpack_to_cart(self):
        self.click(
            self.ADD_BACKPACK_BUTTON
        )

        self.find_visible(
            self.CART_BADGE
        )

    def get_cart_count(self):
        return self.get_text(
            self.CART_BADGE
        )

    def go_to_cart(self):
        cart_url = (
            BASE_URL.rstrip("/")
            + "/cart.html"
        )

        self.open_url(
            cart_url
        )

        self.wait_for_url(
            "cart.html"
        )

    def sort_products(
        self,
        value
    ):
        dropdown_element = self.find(
            self.SORT_DROPDOWN
        )

        dropdown = Select(
            dropdown_element
        )

        dropdown.select_by_value(
            value
        )

    def get_product_prices(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_PRICES
            )
        )

        return [
            float(
                element.text.replace(
                    "$",
                    ""
                )
            )
            for element in elements
        ]
