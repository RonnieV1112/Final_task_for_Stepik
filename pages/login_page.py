from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.is_link(), f'{LoginPageLocators.LOGIN_URL} is not presented in URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'Email input is not presented in login form'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'Password is not presented in login form'
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), 'Login button is not presented in login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), 'Email is not in register form'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), 'Password is not in register form'
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM), 'Confirm password is not in register form'
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT), 'Register button is not in register form'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)
        confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM)
        confirm_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        button.click()



