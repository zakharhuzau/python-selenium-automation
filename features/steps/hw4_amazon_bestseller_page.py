from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLER_PAGE = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers'
FIVE_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')
FIELD_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
SEARCH_BUTTON = (By.CSS_SELECTOR, '#nav-search-submit-button')
HAVE_PRICE = (By.CSS_SELECTOR, '.a-price-whole')
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')


@given('Open BestSeller page')
def open_bestseller_page(context):
    context.driver.get(BESTSELLER_PAGE)


@then('Verify there are 5 links')
def verify_5links(context):
    links = context.driver.find_elements(*FIVE_LINKS)
    links = len(links)
    assert links == 5, f'Error! Expected {links}, but got 5'


@when('Input {product} into Amazon search field')
def input_into_amazon(context, product):
    field_input = context.driver.find_element(*FIELD_INPUT)
    field_input.clear()
    field_input.send_keys(product)


@when('Click on search button')
def click_search_btn(context):
    context.driver.find_element(*SEARCH_BUTTON).click()


@when('Click on any product')
def click_any_product(context):
    products = context.driver.find_elements(*HAVE_PRICE)
    products[0].click()


@when('Click on add to cart button')
def click_addtocart_btn(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()