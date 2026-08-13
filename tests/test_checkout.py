import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import TEST_USERNAME, TEST_PASSWORD


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_successful_checkout(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    products_page.add_backpack_to_cart()

    products_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_information(
        "Yavuzhan",
        "Kiyi",
        "54000"
    )

    checkout_page.click_continue()

    checkout_page.click_finish()

    assert (
        checkout_page.get_complete_message()
        == "Thank you for your order!"
    )


@pytest.mark.ui
@pytest.mark.regression
def test_checkout_without_first_name(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    products_page.add_backpack_to_cart()

    products_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_information(
        "",
        "Kiyi",
        "54000"
    )

    checkout_page.click_continue()

    error_message = (
        checkout_page.get_error_message()
    )

    assert (
        "First Name is required"
        in error_message
    )


@pytest.mark.ui
@pytest.mark.regression
def test_checkout_without_postal_code(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    products_page.add_backpack_to_cart()

    products_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_information(
        "Yavuzhan",
        "Kiyi",
        ""
    )

    checkout_page.click_continue()

    error_message = (
        checkout_page.get_error_message()
    )

    assert (
        "Postal Code is required"
        in error_message
    )

