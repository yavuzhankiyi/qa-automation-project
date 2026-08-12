import pytest

from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        (
            "standard_user",
            "wrong_password",
            "Username and password do not match"
        ),
        (
            "",
            "secret_sauce",
            "Username is required"
        ),
        (
            "standard_user",
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

    assert expected_message in login_page.get_error_message()