from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

CART_BTN = (By.CSS_SELECTOR, "span.menu-btn-text")
ALL_ITEMS_1 = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
EMPTY_CROSS_SIGN = (By.CSS_SELECTOR, "a.deleteCartItemButton.close")

@given("I am on Homepage")
def open_homepage(context):
    context.app.main_page.open_page()

@then('Input "{text}" into search string')
def input_item_into_search_string(context, text):
    context.app.main_page.search_word(text)

@then("Click search button")
def click_search_btn(context):
    context.app.main_page.click_search_button(context)

@then("Verify all items with Table in the title are here")
def chosen_itms_are_here(context):
    context.app.main_page.chosen_items_are_here(context)

@then("Add the last of found items to cart")
def add_last_item_to_cart(context):
    # context.app.main_page.add_last_item_to_cart(context)
    context.driver.find_elements( *ALL_ITEMS_1 )[-1].click()
# wait until pop-up desappears
    sleep(10)

@then("Click on cart button")
def click_on_cart_button(context):
    # context.app.main_page.click_on_cart_button(context)
    context.driver.find_elements( *CART_BTN )[1].click()

@then("Click on cross symbol empty cart")
def click_on_cross_symbl_empty_cart(context):
    context.app.main_page.click_on_cross_symbol_empty_cart(context)

@then("Verify cart is empty")
def verify_crt_is_empty(context):
    context.app.main_page.verify_cart_is_empty(context)