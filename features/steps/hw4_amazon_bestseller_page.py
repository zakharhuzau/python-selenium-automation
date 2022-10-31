from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLER_PAGE = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers'
FIVE_LINKS = (By.CSS_SELECTOR, '#zg_header a')


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
    context.app.main_page.input_into_search(product)


@when('Click on search button')
def click_search_btn(context):
    context.app.main_page.click_search_btn()


@when('Click on any product')
def click_any_product(context):
    context.app.search_result_page.click_any_product()


@when('Click on add to cart button')
def click_addtocart_btn(context):
    context.app.product_page.click_add_to_cart_btn()