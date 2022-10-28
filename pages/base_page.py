from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'
        self.wait = WebDriverWait(self.driver, 15)

    def open_url(self, end_url=''):
        url = f'{self.base_url}{end_url}'
        print(f'Opening URL:{url}')
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.find_element(*locator)
        e.clear()
        e.send_keys(text)
        print(f'Inputting text: {text}')

    def verify_element_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Error! Expected {expected_text}, but got {actual_text}'

    def verify_element(self, element_name, *locator):
        assert self.find_element(*locator), \
            f'Error! {element_name} is not present'

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))