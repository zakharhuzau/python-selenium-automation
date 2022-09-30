from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")

@when('Click orders')
def click_orders(context):
    context.driver.find_element(By.ID, "nav-orders").click()

@then('Verify: Sign In header is visible and email input field is present')
def verify_signin_and_input(context):
    actual_result_sign_in = "Sign in"
    expected_result_sigh_in = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_result_sign_in == expected_result_sigh_in, f'Error! Expected {expected_result_sigh_in}, but got ' \
                                                             f'{actual_result_sign_in}'
    assert context.driver.find_element(By.ID, "ap_email"), f'Error! Email input field is not present'
