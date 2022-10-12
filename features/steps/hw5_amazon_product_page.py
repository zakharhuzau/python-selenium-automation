from behave import given, then
from selenium.webdriver.common.by import By

PRODUCT_IMG = (By.CSS_SELECTOR, '.swatchAvailable img')
PRODUCT_TEXT = (By.CSS_SELECTOR, '.selection')


@given('Open Amazon product page')
def open_amazom_product_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify colors')
def verify_colors(context):
    products = context.driver.find_elements(*PRODUCT_IMG)
    expected_colors = [
        'Black',
        'Blue, Over Dye',
        'Bright White',
        'Dark Blue Vintage',
        'Dark Indigo/Rinsed'
    ]
    actual_colors = []
    for product in products[:5]:
        product.click()
        text = context.driver.find_element(*PRODUCT_TEXT).text
        actual_colors.append(text)

    assert expected_colors == actual_colors, f'Error! Expected colors {expected_colors} ' \
                                             f'did not match actaul colors {actual_colors}'
