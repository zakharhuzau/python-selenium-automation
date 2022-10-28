from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    SEARCH_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
    SEARCH_CONFIRM_ADD_T0_CART = (By.CSS_SELECTOR, '#attach-sidesheet-view-cart-button')

    def click_add_to_cart_btn(self):
        self.click(*self.SEARCH_ADD_TO_CART_BUTTON)
        self.wait_for_element_click(*self.SEARCH_CONFIRM_ADD_T0_CART)
