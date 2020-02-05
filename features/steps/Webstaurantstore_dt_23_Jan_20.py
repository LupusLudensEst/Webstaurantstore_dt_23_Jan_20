from behave import given,then

@given("I am on Homepage")
def open_homepage(context):
    context.app.main_page.open_page()

@then('Input "{text}" into search string')
def input_item_into_search_string(context, text):
    context.app.main_page.search_word(text)

@then("Click search button")
def click_search_btn(context):
    context.app.main_page.click_search_button()

@then("Verify all items with Table in the title are here")
def chosen_itms_are_here(context):
    context.app.main_page.chosen_items_are_here()

@then("Add the last of found items to cart")
def add_last_itm_to_cart(context):
    context.app.main_page.add_last_item_to_cart()

@then("Click on cart button")
def click_on_cart_button(context):
    context.app.main_page.click_on_cart_button()

@then("Click on cross symbol empty cart")
def click_on_cross_symbl_empty_cart(context):
    context.app.main_page.click_on_cross_symbol_empty_cart()

@then("Verify cart is empty")
def verify_crt_is_empty(context):
    context.app.main_page.verify_cart_is_empty()