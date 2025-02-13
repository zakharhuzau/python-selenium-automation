from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultPage(Page):
    SEARCH_HAVE_PRICE = (By.CSS_SELECTOR, '.a-price-whole')

    def click_any_product(self):
        products = self.find_elements(*self.SEARCH_HAVE_PRICE)
        products[0].click()

    def verify_department(self, department):
        celector = (By.CSS_SELECTOR, f'#nav-subnav[data-category="{department}"]')
        self.verify_element(department, *celector)