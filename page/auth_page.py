from playwright.sync_api import Page, expect
from selector import auth_page_selector as aps


def valid_login(page: Page, username: str, password: str):
    page.goto("https://www.saucedemo.com/")

    page.locator(aps.USERNAME_INPUT_TXT).fill(username)
    page.locator(aps.PASSWORD_INPUT_TXT).fill(password)
    page.locator(aps.LOGIN_BTN).click()

    assert page.url == "https://www.saucedemo.com/inventory.html"


def invalid_login(page: Page, username: str, password: str):
    page.goto("https://www.saucedemo.com/")

    page.locator(aps.USERNAME_INPUT_TXT).fill(username)
    page.locator(aps.PASSWORD_INPUT_TXT).fill(password)
    page.locator(aps.LOGIN_BTN).click()

    expect(page.locator(aps.ERROR_LOGIN_MSG)).to_be_visible()


def logout(page: Page):
    page.locator(aps.BURGER_MENU_BTN).click()
    page.locator(aps.LOGOUT_BTN).click()

    assert page.url == "https://www.saucedemo.com/"
