from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    SEARCH_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
    SEARCH_CONFIRM_ADD_T0_CART = (By.CSS_SELECTOR, '#attach-sidesheet-view-cart-button')
    MENU_NEW_ARRIVALS = (By.CSS_SELECTOR, 'a[aria-label="New Arrivals"]')
    SUBMENU_NEW_ARRIVALS = (By.CSS_SELECTOR, 'div[id*="megamenu-8:0"]')

    def open_product_page(self, end_url):
        self.open_url(end_url)

    def hover_over(self):
        menu = self.find_element(*self.MENU_NEW_ARRIVALS)
        action = ActionChains(self.driver)
        action.move_to_element(menu)
        action.perform()

    def verify_user_sees_deals(self):
        self.wait_for_element_click(*self.SUBMENU_NEW_ARRIVALS)

    def click_add_to_cart_btn(self):
        self.click(*self.SEARCH_ADD_TO_CART_BUTTON)
        self.wait_for_element_click(*self.SEARCH_CONFIRM_ADD_T0_CART)
