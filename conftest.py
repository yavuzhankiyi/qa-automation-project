import os
import pytest

from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs(
                "reports/screenshots",
                exist_ok=True
            )

            screenshot_path = (
                f"reports/screenshots/"
                f"{item.name}.png"
            )

            driver.save_screenshot(
                screenshot_path
            )

            print(
                f"\nScreenshot saved: "
                f"{screenshot_path}"
            )