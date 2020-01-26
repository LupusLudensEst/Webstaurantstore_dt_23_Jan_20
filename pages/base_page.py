from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://www.webstaurantstore.com/'

    def click(self, *locator):
        """
        Clicks on WebElement
        :param locator: search strategy for find_element of a Web Element, ex. (By.ID, 'id')
        """
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, url: str=''):
        #logger.info(f'Opening page {self.base_url + url}')
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text  # , f'Expected text {expected_text}, but got {actual_text}'
        #assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'