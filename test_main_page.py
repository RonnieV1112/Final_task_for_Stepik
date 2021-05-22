import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, link)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_message_about_empty_basket()
