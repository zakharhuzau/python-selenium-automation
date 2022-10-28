from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
from pages.search_result_page import SearchResultPage
from pages.product_page import ProductPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.product_page = ProductPage(self.driver)