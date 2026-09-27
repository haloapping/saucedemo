from enum import StrEnum

from playwright.sync_api import Page, expect

from selector import inventory_page_selector as ips


class SORT_BY(StrEnum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    PRICE_ASC = "price_asc"
    PRICE_DESC = "price_desc"


def sort_product(page: Page, sort_by: SORT_BY):
    match sort_by:
        case SORT_BY.NAME_ASC:
            page.select_option(ips.SORT_PRODUCT_SELECT_OPTION, value="az")
            expect(page.locator(ips.SORT_PRODUCT_SELECT_OPTION)).to_have_value("az")
        case SORT_BY.NAME_DESC:
            page.select_option(ips.SORT_PRODUCT_SELECT_OPTION, value="za")
            expect(page.locator(ips.SORT_PRODUCT_SELECT_OPTION)).to_have_value("za")
        case SORT_BY.PRICE_ASC:
            page.select_option(ips.SORT_PRODUCT_SELECT_OPTION, value="lohi")
            expect(page.locator(ips.SORT_PRODUCT_SELECT_OPTION)).to_have_value("lohi")
        case SORT_BY.PRICE_DESC:
            page.select_option(ips.SORT_PRODUCT_SELECT_OPTION, value="hilo")
            expect(page.locator(ips.SORT_PRODUCT_SELECT_OPTION)).to_have_value("hilo")


def add_to_cart(page: Page):
    page.get_by_text(ips.ADD_TO_CART_BTN).nth(0).click()
    expect(page.locator(ips.NUMBER_OF_CART_ICON)).to_have_text("1")

    page.get_by_text(ips.ADD_TO_CART_BTN).nth(1).click()
    expect(page.locator(ips.NUMBER_OF_CART_ICON)).to_have_text("2")

    page.locator(ips.CART_BTN).click()
