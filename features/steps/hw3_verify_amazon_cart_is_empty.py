from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click Cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()

@then('Verify Amazon Cart')
def verify_amazon_cart(context):
    expected = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert expected == "0", f'Error! Expected {expected}, but got "0"'