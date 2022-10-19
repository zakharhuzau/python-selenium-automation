from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL_TC = 'https://www.amazon.com/gp/help/customer/display.html/' \
         'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
PRIVACE_NOTICE = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')
BEST_SELLER_LINK = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
BEST_SELLERS_LINKS = (By.CSS_SELECTOR, 'div[class*="zg-nav-tab-all"] a')
BEST_SELLER_HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get(URL_TC)


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_amazon_pn_link(context):
    context.driver.find_element(*PRIVACE_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_new_open_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_pn_page_is_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@then('User can close new window and switch back to original')
def close_new_window_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


@when('Click on Best Sellers link')
def click_on_best_seller_link(context):
    context.driver.find_element(*BEST_SELLER_LINK).click()


@then('Clicks on each top links and verifies these')
def verifies_best_sellers_links(context):
    i = 0
    while True:
        links = context.driver.find_elements(*BEST_SELLERS_LINKS)
        text_link = links[i].text
        links[i].click()
        header = context.driver.find_element(*BEST_SELLER_HEADER).text
        assert  text_link in header, 'Error! Text of the link does not contain in the header text'
        i += 1
        if i == len(links):
            break