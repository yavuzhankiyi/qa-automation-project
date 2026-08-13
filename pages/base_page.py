from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout
        )

    def open_url(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

    def find_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

        element.click()

    def js_click(self, locator):
        element = self.find(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def type_text(self, locator, text):
        element = self.find_visible(
            locator
        )

        element.clear()

        if text:
            element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(
            locator
        ).text

    def get_attribute(
        self,
        locator,
        attribute
    ):
        return self.find(
            locator
        ).get_attribute(
            attribute
        )

    def is_present(self, locator):
        elements = self.driver.find_elements(
            *locator
        )

        return len(elements) > 0

    def wait_until_invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(
                locator
            )
        )

    def wait_for_url(self, text):
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
