from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    SEARCH_STRING = (By.ID, "searchval")
    SEARCH_BTN = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
    ALL_ITEMS_1 = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
    ALL_ITEMS_2 = (By.CSS_SELECTOR, "a.description")
    PRODUCTS = (By.CSS_SELECTOR, '.ag-item.gtm-product')
    CART_BTN = (By.CSS_SELECTOR, "span.menu-btn-text")
    EMPTY_CROSS_SIGN = (By.CSS_SELECTOR, "a.deleteCartItemButton.close")
    CART_ITEM = (By.ID, "cartItemCountSpan")