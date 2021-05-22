from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def click_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_name_of_product_in_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), 'Success alert is not presented'
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name = product.text
        alert = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text
        assert name == alert, f'Expected {name}, got {alert}'

    def should_be_product_price_in_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_ALERT), 'Price alert is not presented'
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = product.text
        alert = self.browser.find_element(*ProductPageLocators.PRICE_ALERT).text
        assert price == alert, f'Expected {price}, got {alert}'
