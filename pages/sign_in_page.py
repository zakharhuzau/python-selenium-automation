from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SEARCH_SIGNIN_HEADER = (By.XPATH, '//h1[@class="a-spacing-small"]')
    SEARCH_EMAIL_INPUT = (By.ID, 'ap_email')

    def verify_sign_in_header(self):
        expected_text = 'Sign in'
        self.verify_element_text(expected_text, *self.SEARCH_SIGNIN_HEADER)

    def verify_email_input_element(self):
        self.verify_element('Email input field', *self.SEARCH_EMAIL_INPUT)