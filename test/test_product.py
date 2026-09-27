from playwright.sync_api import Page

from page import auth_page, inventory_page
from page.auth_page import LoginCredential
from page.inventory_page import SORT_BY


def test_sort_porduct_by(page: Page):
    lc = LoginCredential(
        username="standard_user",
        password="secret_sauce",
    )
    auth_page.valid_login(page, lc)

    inventory_page.sort_product(page, SORT_BY.NAME_ASC)
    inventory_page.sort_product(page, SORT_BY.NAME_DESC)
    inventory_page.sort_product(page, SORT_BY.PRICE_ASC)
    inventory_page.sort_product(page, SORT_BY.PRICE_DESC)

    auth_page.logout(page)
