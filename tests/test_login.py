import pytest

from pages.login_page import LoginPage

from config.config import (
    TEST_USERNAME,
    TEST_PASSWORD
)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    assert "inventory" in driver.current_url


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        (
            TEST_USERNAME,
            "wrong_password",
            "Username and password do not match"
        ),
        (
            "",
            TEST_PASSWORD,
            "Username is required"
        ),
        (
            TEST_USERNAME,
            "",
            "Password is required"
        ),
        (
            "",
            "",
            "Username is required"
        ),
    ]
)
def test_invalid_login(
    driver,
    username,
    password,
    expected_message
):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        username,
        password
    )

    assert (
        expected_message
        in login_page.get_error_message()
    )
