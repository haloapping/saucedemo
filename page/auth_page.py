from dataclasses import dataclass
import os

from playwright.sync_api import Page, expect

from selector import auth_page_selector as aps

from dotenv import load_dotenv


@dataclass
class LoginCredential:
    username: str
    password: str


def valid_login(page: Page, lc: LoginCredential):
    load_dotenv()
    page.goto(os.getenv("BASE_URL"))

    page.locator(aps.USERNAME_INPUT_TXT).fill(lc.username)
    page.locator(aps.PASSWORD_INPUT_TXT).fill(lc.password)
    page.locator(aps.LOGIN_BTN).click()

    assert page.url == "https://www.saucedemo.com/inventory.html"


def invalid_login(page: Page, lc: LoginCredential):
    load_dotenv()
    page.goto(os.getenv("BASE_URL"))

    page.locator(aps.USERNAME_INPUT_TXT).fill(lc.username)
    page.locator(aps.PASSWORD_INPUT_TXT).fill(lc.password)
    page.locator(aps.LOGIN_BTN).click()

    expect(page.locator(aps.ERROR_LOGIN_MSG)).to_be_visible()


def logout(page: Page):
    page.locator(aps.BURGER_MENU_BTN).click()
    page.locator(aps.LOGOUT_BTN).click()

    assert page.url == "https://www.saucedemo.com/"
