from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_BACKPACK_BUTTON
            )
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.CART_BADGE
            )
        ).text

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CART_LINK
            )
        ).click()

    def sort_products(self, value):
        dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(
                    self.SORT_DROPDOWN
                )
            )
        )

        dropdown.select_by_value(value)

    def get_product_prices(self):
        price_elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_PRICES
            )
        )

        return [
            float(element.text.replace("$", ""))
            for element in price_elements
        ]