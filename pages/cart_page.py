from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    SEARCH_CART_COUNT = (By.ID, 'nav-cart-count')

    def verify_cart_count(self, expected_text):
        self.verify_element_text(expected_text, *self.SEARCH_CART_COUNT)