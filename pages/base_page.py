from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            timeout
        )

        self.logger = get_logger(
            self.__class__.__name__
        )

    def open_url(self, url):
        self.logger.info(
            f"Opening URL: {url}"
        )

        self.driver.get(
            url
        )

    def find(self, locator):
        self.logger.info(
            f"Waiting for element: {locator}"
        )

        return self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

    def find_visible(self, locator):
        self.logger.info(
            f"Waiting for visible element: {locator}"
        )

        return self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

    def click(self, locator):
        self.logger.info(
            f"Clicking element: {locator}"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

        element.click()

    def js_click(self, locator):
        self.logger.info(
            f"JavaScript click: {locator}"
        )

        element = self.find(
            locator
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def type_text(
        self,
        locator,
        text
    ):
        self.logger.info(
            f"Typing text into element: {locator}"
        )

        element = self.find_visible(
            locator
        )

        element.clear()

        if text:
            element.send_keys(
                text
            )

    def get_text(self, locator):
        self.logger.info(
            f"Reading text from element: {locator}"
        )

        return self.find_visible(
            locator
        ).text

    def get_attribute(
        self,
        locator,
        attribute
    ):
        self.logger.info(
            f"Reading attribute '{attribute}' from: {locator}"
        )

        return self.find(
            locator
        ).get_attribute(
            attribute
        )

    def is_present(self, locator):
        elements = self.driver.find_elements(
            *locator
        )

        result = len(elements) > 0

        self.logger.info(
            f"Element present {locator}: {result}"
        )

        return result

    def wait_until_invisible(
        self,
        locator
    ):
        self.logger.info(
            f"Waiting until element becomes invisible: {locator}"
        )

        return self.wait.until(
            EC.invisibility_of_element_located(
                locator
            )
        )

    def wait_for_url(self, text):
        self.logger.info(
            f"Waiting for URL containing: {text}"
        )

        return self.wait.until(
            EC.url_contains(
                text
            )
        )

    def set_input_value(
        self,
        locator,
        value
    ):
        self.logger.info(
            f"Setting input value: {locator}"
        )

        element = self.find_visible(
            locator
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

            setter.call(
                element,
                value
            );

            element.dispatchEvent(
                new Event(
                    'input',
                    { bubbles: true }
                )
            );

            element.dispatchEvent(
                new Event(
                    'change',
                    { bubbles: true }
                )
            );
            """,
            element,
            value
        )

        self.wait.until(
            lambda driver:
                driver.find_element(
                    *locator
                ).get_attribute(
                    "value"
                ) == value
        )
