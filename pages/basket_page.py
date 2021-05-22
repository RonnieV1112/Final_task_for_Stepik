from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert BasketPageLocators.BASKET_URL in self.is_link(), \
            f'{BasketPageLocators.BASKET_URL} is not presented in URL'

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            'Basket item is presented, but should not be'

    def should_be_message_about_empty_basket(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert message == BasketPageLocators.MESSAGE_TEXT, \
            f'Expected message: {BasketPageLocators.MESSAGE_TEXT}, got message: {message}'
