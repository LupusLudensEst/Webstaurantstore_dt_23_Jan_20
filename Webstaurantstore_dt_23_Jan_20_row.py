from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

SEARCH_STRING = (By.ID, "searchval")
SEARCH_BTN = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
ALL_ITEMS_1 = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
ALL_ITEMS_2 = (By.CSS_SELECTOR, "a.description")
PRODUCTS = (By.CSS_SELECTOR, '.ag-item.gtm-product')
CART_BTN = (By.CSS_SELECTOR, "span.menu-btn-text")
EMPTY_CROSS_SIGN = (By.CSS_SELECTOR, "a.deleteCartItemButton.close")
CART_ITEM = (By.ID, "cartItemCountSpan")

# I am on Homepage
driver.get( 'https://www.webstaurantstore.com/' )


# Input item into search string
search = driver.find_element( *SEARCH_STRING )
search.clear()
search.send_keys( 'stainless work table' )


# Click search button
driver.find_element( *SEARCH_BTN  ).click()


# Verify all items with Table in the title are here
print('There are : ', len(driver.find_elements( *ALL_ITEMS_1 )), 'items.')
print('There are : ', len(driver.find_elements( *ALL_ITEMS_2 )), 'descriptions.')
products = driver.find_elements( *PRODUCTS )
for product in list(products):
    title = product.find_element( *ALL_ITEMS_2 )
    assert 'Table' in title.text
print('Title:', title.text, '.')


# Add the last of found items to cart
driver.find_elements( *ALL_ITEMS_1 )[-1].click()
# wait until pop-up desappears
sleep(10)


# Click on cart button
driver.find_elements( *CART_BTN )[1].click()


# Click on cross symbol empty cart
driver.find_element( *EMPTY_CROSS_SIGN ).click()
# wait until cart is empthy
sleep(10)


# Verify cart is empty
driver.find_element( *CART_ITEM ).text
print('Text in the cart button: ', str(driver.find_element( *CART_ITEM ).text),'.')

# exit
driver.quit()