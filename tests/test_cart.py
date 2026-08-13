import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_add_product_to_cart(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"

    products_page.go_to_cart()

    assert (
        cart_page.get_item_name()
        == "Sauce Labs Backpack"
    )


@pytest.mark.ui
@pytest.mark.regression
def test_remove_product_from_cart(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"

    products_page.go_to_cart()

    assert (
        cart_page.get_item_name()
        == "Sauce Labs Backpack"
    )

    cart_page.remove_item()

    assert (
        cart_page.is_item_present()
        is False
    )
