from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    SEARCH_STRING = (By.ID, "searchval")
    SEARCH_BTN = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
    ITEMS_TO_CHOOSE = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
    ITEMS_DESCRIPTIONS = (By.CSS_SELECTOR, "a.description")
    PRODUCTS = (By.CSS_SELECTOR, '.ag-item.gtm-product')
    CART_BTN = (By.CSS_SELECTOR, "span.menu-btn-text")
    EMPTY_CROSS_SIGN = (By.CSS_SELECTOR, "a.deleteCartItemButton.close")
    CART_ITEM = (By.ID, "cartItemCountSpan")

# 1.Input "{text}" into search string
    def search_word(self, text):
        self.input_text( text, *self.SEARCH_STRING)

# 2.Click search button
    def click_search_button(self, context):
        self.click(*self.SEARCH_BTN)

# 3.Verify all items with Table in the title are here
    def chosen_items_are_here(self, context):
        print('There are : ', len(context.driver.find_elements(*self.ITEMS_TO_CHOOSE)), 'items.')
        print('There are : ', len(context.driver.find_elements(*self.ITEMS_DESCRIPTIONS)), 'descriptions.')
        products = self.driver.find_elements(*self.PRODUCTS)
        for product in list(products):
            title = product.find_element(*self.ITEMS_DESCRIPTIONS)
            assert 'Table' in title.text
        print('Title:', title.text, '.')
        # wait until cart is empthy
        sleep(10)

# # 4.Add the last of found items to cart
#     def add_last_item_to_cart(self, context):
#         self.click(*self.ITEMS_TO_CHOOSE)[-1]
# # wait until pop-up desappears
#         sleep(10)

# # 5.Click on cart button
#     def click_on_cart_button(self, context):
#         self.click(*self.CART_BTN)[1]

# 6.Click on cross symbol empty cart
    def click_on_cross_symbol_empty_cart(self, context):
        self.click(*self.EMPTY_CROSS_SIGN)
# wait until cart is empthy
        sleep(10)

# 7.Verify cart is empty
    def verify_cart_is_empty(self, context):
        assert '0' in self.driver.find_element(*self.CART_ITEM).text
        print('Text in the cart button: ', str(context.driver.find_element(*self.CART_ITEM).text), '.')