from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given("I am on Homepage")
def open_homepage(context):
    context.driver.get( 'https://www.webstaurantstore.com/' )


@then("Input item into search string")
def input_item_into_search_string(context):
    search = context. driver.find_element( By.ID, "searchval" )
    search.clear()
    search.send_keys( 'stainless work table' )


@then("Click search button")
def click_search_button(context):
    context.driver.find_element( By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn" ).click()


@then("Verify all items with Table in the title are here")
def chosen_items_are_here(context):
    print('There are : ', len(context.driver.find_elements(By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")), 'items.')
    assert 'Table' in context.driver.find_element(By.CSS_SELECTOR, "a.description").text
    print('There are : ', len(context.driver.find_elements(By.CSS_SELECTOR, "a.description")), 'descriptions.')
    print('Table is here: ', str(context.driver.find_element(By.CSS_SELECTOR, "a.description").text), '.')


@then("Add the last of found items to cart")
def add_last_item_to_cart(context):
    context.driver.find_elements( By.CSS_SELECTOR, "input.btn.btn-cart.btn-small" )[-1].click()
# wait until pop-up desappears
    sleep(10)


@then("Click on cart button")
def click_on_cart_button(context):
    context.driver.find_elements( By.CSS_SELECTOR, "span.menu-btn-text" )[1].click()


@then("Click on cross symbol empty cart")
def click_on_cross_symbol_empty_cart(context):
    context.driver.find_element( By.CSS_SELECTOR, "a.deleteCartItemButton.close" ).click()
# wait until cart is empthy
    sleep(10)


@then("Verify cart is empty")
def verify_cart_is_empty(context):
    assert '0' in context.driver.find_element(By.ID, "cartItemCountSpan").text
    print('Text in the cart button: ', str(context.driver.find_element(By.ID, "cartItemCountSpan").text), '.')

    #context.driver.quit()