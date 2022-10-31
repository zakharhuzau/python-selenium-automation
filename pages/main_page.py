from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    ORDERS_BUTTON = (By.ID, 'nav-orders')
    CART_BUTTON = (By.CSS_SELECTOR, '#nav-cart')
    SEARCH_FIELD_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#nav-search-submit-button')
    DEPARTMENT = (By.ID, 'searchDropdownBox')
    def open_main(self):
        self.open_url()

    def click_orders(self):
        self.click(*self.ORDERS_BUTTON)

    def click_cart(self):
        self.click(*self.CART_BUTTON)

    def input_into_search(self, search_text):
        self.input_text(search_text, *self.SEARCH_FIELD_INPUT)

    def click_search_btn(self):
        self.click(*self.SEARCH_BUTTON)

    def select_department(self, department):
        select = Select(self.find_element(*self.DEPARTMENT))
        select.select_by_value(f'search-alias={department}')