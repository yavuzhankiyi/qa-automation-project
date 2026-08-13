import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

from config.config import (
    TEST_USERNAME,
    TEST_PASSWORD
)

from utils.data_loader import (
    load_test_data
)


TEST_DATA = load_test_data()

PRODUCT_DATA = (
    TEST_DATA["product"]["backpack"]
)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_add_product_to_cart(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    products_page.add_backpack_to_cart()

    assert (
        products_page.get_cart_count()
        == PRODUCT_DATA["cart_count"]
    )

    products_page.go_to_cart()

    assert (
        cart_page.get_item_name()
        == PRODUCT_DATA["name"]
    )


@pytest.mark.ui
@pytest.mark.regression
def test_remove_product_from_cart(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    products_page.add_backpack_to_cart()

    assert (
        products_page.get_cart_count()
        == PRODUCT_DATA["cart_count"]
    )

    products_page.go_to_cart()

    assert (
        cart_page.get_item_name()
        == PRODUCT_DATA["name"]
    )

    cart_page.remove_item()

    assert (
        cart_page.is_item_present()
        is False
    )
