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

    def enter_first_name(self, first_name):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        )

        element.clear()
        element.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.POSTAL_CODE
            )
        )

        element.clear()

        if postal_code:
            element.send_keys(postal_code)

    def fill_checkout_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.wait_for_checkout_page()

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        continue_button = self.wait.until(
            EC.presence_of_element_located(
                self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            continue_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        # Continue sonrası iki geçerli ihtimal var:
        # 1 - Geçerli bilgiler -> step two
        # 2 - Eksik bilgiler -> error message
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
        # Önce overview sayfasına gerçekten
        # geçtiğimizden emin oluyoruz.
        self.wait.until(
            EC.url_contains(
                "checkout-step-two.html"
            )
        )

        finish_button = self.wait.until(
            EC.presence_of_element_located(
                self.FINISH_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            finish_button
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
        complete_message = self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        )

        return complete_message.text