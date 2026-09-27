from playwright.sync_api import Page

from page import auth_page, cart_page, checkout_page, inventory_page
from page.checkout_page import YourInformation


def test_fully_transaction_success(page: Page):
    auth_page.valid_login(page, "standard_user", "secret_sauce")
    inventory_page.add_to_cart(page)
    cart_page.checkout(page)
    checkout_page.check_your_information(
        page,
        YourInformation(
            first_name="Alfiyanto",
            last_name="Kondolele",
            postal_code="909090",
        ),
    )
    checkout_page.checkout_overview(page)
    checkout_page.checkout_complete(page)
    auth_page.logout(page)
