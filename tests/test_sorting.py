import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

from config.config import (
    TEST_USERNAME,
    TEST_PASSWORD
)

from utils.data_loader import (
    load_test_data
)


TEST_DATA = load_test_data()

SORTING_DATA = (
    TEST_DATA["sorting"]
)


@pytest.mark.ui
@pytest.mark.regression
def test_sort_price_low_to_high(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    products_page.sort_products(
        SORTING_DATA["low_to_high"]
    )

    prices = (
        products_page.get_product_prices()
    )

    assert prices == sorted(
        prices
    )


@pytest.mark.ui
@pytest.mark.regression
def test_sort_price_high_to_low(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open()

    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    products_page.sort_products(
        SORTING_DATA["high_to_low"]
    )

    prices = (
        products_page.get_product_prices()
    )

    assert prices == sorted(
        prices,
        reverse=True
    )
