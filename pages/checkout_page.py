from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    COMPLETE_HEADER = (
        By.CSS_SELECTOR,
        "[data-test='complete-header']"
    )

    def wait_for_checkout_page(self):
        self.wait_for_url(
            "checkout-step-one.html"
        )

        self.find_visible(
            self.FIRST_NAME
        )

    def enter_first_name(
        self,
        first_name
    ):
        self.set_input_value(
            self.FIRST_NAME,
            first_name
        )

    def enter_last_name(
        self,
        last_name
    ):
        self.set_input_value(
            self.LAST_NAME,
            last_name
        )

    def enter_postal_code(
        self,
        postal_code
    ):
        self.set_input_value(
            self.POSTAL_CODE,
            postal_code
        )

    def fill_checkout_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.wait_for_checkout_page()

        self.enter_first_name(
            first_name
        )

        self.enter_last_name(
            last_name
        )

        self.enter_postal_code(
            postal_code
        )

    def click_continue(self):
        self.js_click(
            self.CONTINUE_BUTTON
        )

        self.wait.until(
            lambda driver:
                "checkout-step-two.html"
                in driver.current_url
                or self.is_present(
                    self.ERROR_MESSAGE
                )
        )

    def click_finish(self):
        self.wait_for_url(
            "checkout-step-two.html"
        )

        self.js_click(
            self.FINISH_BUTTON
        )

        self.wait_for_url(
            "checkout-complete.html"
        )

    def get_error_message(self):
        return self.get_text(
            self.ERROR_MESSAGE
        )

    def get_complete_message(self):
        return self.get_text(
            self.COMPLETE_HEADER
        )
