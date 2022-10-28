from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Click orders')
def click_orders(context):
    context.app.main_page.click_orders()


@then('Verify: Sign In header is visible and email input field is present')
def verify_signin_and_input(context):
    context.app.sign_in_page.verify_sign_in_header()
    context.app.sign_in_page.verify_email_input_element()