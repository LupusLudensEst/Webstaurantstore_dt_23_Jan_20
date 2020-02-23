from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    # locators
    SEARCH_STRING = (By.ID, "searchval")
    SEARCH_BTN = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
    ITEMS_TO_CHOOSE = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
    ITEMS_DESCRIPTIONS = (By.CSS_SELECTOR, "a.description")
    PRODUCTS = (By.CSS_SELECTOR, '.ag-item.gtm-product')
    CART_BTN = (By.CSS_SELECTOR, "a[href*='viewcart'] span.btn-primary")
    EMPTY_CROSS_SIGN = (By.CSS_SELECTOR, "a.deleteCartItemButton.close")
    CART_ITEM = (By.ID, "cartItemCountSpan")
    CARD_EMPTY_BLOCK = (By.CSS_SELECTOR, "div.cartEmpty")

    def search_word(self, text):
        """
        Input "{text}" into search string
        """
        self.input_text( text, *self.SEARCH_STRING)

    def click_search_button(self):
        """
        Click search button
        """
        self.click(*self.SEARCH_BTN)

    def chosen_items_are_here(self):
        """
        Verify all items with Table in the title are here
        """
        print('There are : ', len(self.driver.find_elements(*self.ITEMS_TO_CHOOSE)), 'items.')
        print('There are : ', len(self.driver.find_elements(*self.ITEMS_DESCRIPTIONS)), 'descriptions.')
        products = self.driver.find_elements(*self.PRODUCTS)
        for product in list(products):
            title = product.find_element(*self.ITEMS_DESCRIPTIONS)
            assert 'Table' in title.text
        print('Title:', title.text, '.')
        # wait until cart is empthy
        sleep(10)

    def add_last_item_to_cart(self):
        """
        Add the last of found items to cart
        """
        self.driver.find_elements(*self.ITEMS_TO_CHOOSE)[-1].click()
        sleep(10)

    def click_on_cart_button(self):
        """
        Click on cart button
        """
        self.click(*self.CART_BTN)

    def click_on_cross_symbol_empty_cart(self):
        """
        Click on cross symbol empty cart
        """
        self.click(*self.EMPTY_CROSS_SIGN)
        self.wait_for_element_to_disappear(*self.EMPTY_CROSS_SIGN)

    def verify_cart_is_empty(self):
        """
        Verify cart is empty
        """
        self.wait_for_element_to_be_visible(*self.CARD_EMPTY_BLOCK)
        cart = self.driver.find_element(*self.CART_ITEM)