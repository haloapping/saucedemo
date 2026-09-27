from playwright.sync_api import Page, expect
from selector import inventory_page_selector as ips


def add_to_cart(page: Page):
    page.get_by_text(ips.ADD_TO_CART_BTN).nth(0).click()
    expect(page.locator(ips.NUMBER_OF_CART_ICON)).to_have_text("1")

    page.get_by_text(ips.ADD_TO_CART_BTN).nth(1).click()
    expect(page.locator(ips.NUMBER_OF_CART_ICON)).to_have_text("2")

    page.locator(ips.CART_BTN).click()
