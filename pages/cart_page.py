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
        return self.wait.until(
            EC.visibility_of_element_located(
                self.ITEM_NAME
            )
        ).text

    def remove_item(self):
        remove_button = self.wait.until(
            EC.element_to_be_clickable(
                self.REMOVE_BUTTON
            )
        )

        remove_button.click()

    def is_item_present(self):
        items = self.driver.find_elements(
            *self.ITEM_NAME
        )

        return len(items) > 0

    def click_checkout(self):

        # Önce gerçekten cart sayfasında olduğumuzu kontrol ediyoruz
        self.wait.until(
            EC.url_contains("cart.html")
        )

        # Checkout butonunun DOM içerisinde oluşmasını bekliyoruz
        checkout_button = self.wait.until(
            EC.presence_of_element_located(
                self.CHECKOUT_BUTTON
            )
        )

        # Headless modda görünür alana getiriyoruz
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            checkout_button
        )

        # Normal click yerine JavaScript click
        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        # Checkout form sayfasının açıldığını doğruluyoruz
        self.wait.until(
            EC.url_contains(
                "checkout-step-one.html"
            )
        )