from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

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

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_checkout_page(self):
        self.wait.until(
            EC.url_contains(
                "checkout-step-one.html"
            )
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

    def set_input_value(self, locator, value):
        element = self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            """
            const element = arguments[0];
            const value = arguments[1];

            const setter =
                Object.getOwnPropertyDescriptor(
                    HTMLInputElement.prototype,
                    'value'
                ).set;

            setter.call(element, value);

            element.dispatchEvent(
                new Event('input', { bubbles: true })
            );

            element.dispatchEvent(
                new Event('change', { bubbles: true })
            );
            """,
            element,
            value
        )

        self.wait.until(
            lambda driver:
                driver.find_element(
                    *locator
                ).get_attribute("value")
                == value
        )

    def enter_first_name(self, first_name):
        self.set_input_value(
            self.FIRST_NAME,
            first_name
        )

    def enter_last_name(self, last_name):
        self.set_input_value(
            self.LAST_NAME,
            last_name
        )

    def enter_postal_code(self, postal_code):
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
        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        self.wait.until(
            lambda driver:
                "checkout-step-two.html"
                in driver.current_url
                or len(
                    driver.find_elements(
                        *self.ERROR_MESSAGE
                    )
                ) > 0
        )

    def click_finish(self):
        self.wait.until(
            EC.url_contains(
                "checkout-step-two.html"
            )
        )

        finish_button = self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            finish_button
        )

        self.wait.until(
            EC.url_contains(
                "checkout-complete.html"
            )
        )

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        return error.text

    def get_complete_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        )

        return message.text