import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.ui
@pytest.mark.regression
def test_sort_price_low_to_high(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.sort_products(
        "lohi"
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
        "standard_user",
        "secret_sauce"
    )

    products_page.sort_products(
        "hilo"
    )

    prices = (
        products_page.get_product_prices()
    )

    assert prices == sorted(
        prices,
        reverse=True
    )
