from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductsPage:

    ADD_BACKPACK_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    SORT_DROPDOWN = (
        By.CLASS_NAME,
        "product_sort_container"
    )

    PRODUCT_PRICES = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(
            *self.ADD_BACKPACK_BUTTON
        ).click()

    def get_cart_count(self):
        return self.driver.find_element(
            *self.CART_BADGE
        ).text

    def go_to_cart(self):
        self.driver.find_element(
            *self.CART_LINK
        ).click()

    def sort_products(self, value):
        dropdown = Select(
            self.driver.find_element(
                *self.SORT_DROPDOWN
            )
        )

        dropdown.select_by_value(value)

    def get_product_prices(self):
        price_elements = self.driver.find_elements(
            *self.PRODUCT_PRICES
        )

        return [
            float(element.text.replace("$", ""))
            for element in price_elements
        ]