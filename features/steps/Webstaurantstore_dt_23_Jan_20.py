from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

SEARCH_STRING = (By.ID, "searchval")
SEARCH_BTN = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
ALL_ITEMS_1 = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
ALL_ITEMS_2 = (By.CSS_SELECTOR, "a.description")
PRODUCTS = (By.CSS_SELECTOR, '.ag-item.gtm-product')
CART_BTN = (By.CSS_SELECTOR, "span.menu-btn-text")
EMPTY_CROSS_SIGN = (By.CSS_SELECTOR, "a.deleteCartItemButton.close")
CART_ITEM = (By.ID, "cartItemCountSpan")

@given("I am on Homepage")
def open_homepage(context):
    context.app.main_page.open_page()


@then('Input "stainless work table" into search string')
def input_item_into_search_string(context):
    search = context. driver.find_element( *SEARCH_STRING )
    search.clear()
    search.send_keys( 'stainless work table' )


@then("Click search button")
def click_search_button(context):
    context.driver.find_element( *SEARCH_BTN  ).click()


@then("Verify all items with Table in the title are here")
def chosen_items_are_here(context):
    print('There are : ', len(context.driver.find_elements( *ALL_ITEMS_1 )), 'items.')
    print('There are : ', len(context.driver.find_elements( *ALL_ITEMS_2 )), 'descriptions.')
    products = context.driver.find_elements( *PRODUCTS )
    for product in list(products):
        title = product.find_element( *ALL_ITEMS_2 )
        assert 'Table' in title.text
    print('Title:', title.text, '.')


@then("Add the last of found items to cart")
def add_last_item_to_cart(context):
    context.driver.find_elements( *ALL_ITEMS_1 )[-1].click()
# wait until pop-up desappears
    sleep(10)


@then("Click on cart button")
def click_on_cart_button(context):
    context.driver.find_elements( *CART_BTN )[1].click()


@then("Click on cross symbol empty cart")
def click_on_cross_symbol_empty_cart(context):
    context.driver.find_element( *EMPTY_CROSS_SIGN ).click()
# wait until cart is empthy
    sleep(10)


@then("Verify cart is empty")
def verify_cart_is_empty(context):
    assert '0' in context.driver.find_element( *CART_ITEM ).text
    print('Text in the cart button: ', str(context.driver.find_element( *CART_ITEM ).text), '.')