from dataclasses import dataclass

from playwright.sync_api import Page

from selector import checkout_page_selector as cps


@dataclass
class YourInformation:
    first_name: str
    last_name: str
    postal_code: str


def check_your_information(page: Page, yi: YourInformation):
    page.locator(cps.FIRST_NAME_INPUT_TXT).fill(yi.first_name)
    page.locator(cps.LAST_NAME_INPUT_TXT).fill(yi.last_name)
    page.locator(cps.POSTAL_CODE_INPUT_TXT).fill(yi.postal_code)
    page.locator(cps.CONTINUE_BTN).click()


def checkout_overview(page: Page):
    page.locator(cps.FINISH_BTN).click()


BACK_TO_HOME_BTN = "#back-to-products"


def checkout_complete(page: Page):
    page.locator(BACK_TO_HOME_BTN).click()
