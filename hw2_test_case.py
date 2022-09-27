from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://www.amazon.com/")

driver.find_element(By.ID, "nav-orders").click()

actual_result_sign_in = "Sign in"
expected_result_sigh_in = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert actual_result_sign_in == expected_result_sigh_in, f'Error! Expected {expected_result_sigh_in}, but got ' \
                                                         f'{actual_result_sign_in}'
print('Verify: Sign In header is visible')
expected_result_email = ''
expected_result_email = driver.find_element(By.ID, "ap_email")
assert expected_result_email != '', f'Error! Email input field is not present'
print('Verify: Email input field is present')

driver.quit()
