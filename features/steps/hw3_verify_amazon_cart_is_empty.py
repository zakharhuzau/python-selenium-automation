from behave import given, when, then


@when('Click Cart')
def click_cart(context):
    context.app.main_page.click_cart()


@then('Verify Amazon Cart({count})')
def verify_amazon_cart(context, count):
    context.app.cart_page.verify_cart_count(count)