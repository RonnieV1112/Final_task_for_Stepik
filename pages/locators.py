from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")
    LOGIN_URL = "/accounts/login/"
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"