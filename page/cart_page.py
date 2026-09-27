from playwright.sync_api import Page
from selector import cart_page_selector as cps


def checkout(page: Page):
    page.locator(cps.CHECKOUT_BTN).click()
