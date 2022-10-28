from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_ORDERS = (By.ID, 'nav-orders')
    SEARCH_CART = (By.CSS_SELECTOR, '#nav-cart')
    SEARCH_FIELD_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#nav-search-submit-button')

    def open_main(self):
        self.open_url()

    def click_orders(self):
        self.click(*self.SEARCH_ORDERS)

    def click_cart(self):
        self.click(*self.SEARCH_CART)

    def input_into_search(self, search_text):
        self.input_text(search_text, *self.SEARCH_FIELD_INPUT)

    def click_search_btn(self):
        self.click(*self.SEARCH_BUTTON)