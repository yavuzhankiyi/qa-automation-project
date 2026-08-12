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
        self.wait = WebDriverWait(driver, 15)

    def add_backpack_to_cart(self):

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_BACKPACK_BUTTON
            )
        )

        add_button.click()

    def get_cart_count(self):

        badge = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_BADGE
            )
        )

        return badge.text

    def go_to_cart(self):

        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                self.CART_LINK
            )
        )

        cart_link.click()

        self.wait.until(
            EC.url_contains(
                "cart.html"
            )
        )

    def sort_products(self, value):

        dropdown_element = self.wait.until(
            EC.presence_of_element_located(
                self.SORT_DROPDOWN
            )
        )

        dropdown = Select(
            dropdown_element
        )

        dropdown.select_by_value(
            value
        )

    def get_product_prices(self):

        price_elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_PRICES
            )
        )

        prices = []

        for element in price_elements:
            price = element.text.replace(
                "$",
                ""
            )

            prices.append(
                float(price)
            )

        return prices