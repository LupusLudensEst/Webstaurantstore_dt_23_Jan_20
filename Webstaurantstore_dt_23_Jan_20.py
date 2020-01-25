from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# SEARCH_STRING = (By.XPATH, "//input[@name='searchval']")
# SEARCH_STRING = By.ID, "searchval"
# SEARCH_BTN = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
# ALL_ITEMS_1 = (By.CSS_SELECTOR, "a.description")
# ALL_ITEMS_2 = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
#CART_BTN = (By.CSS_SELECTOR,  "a.menu-btn")
# EMPTHY_CART_BTN_1 = (By.XPATH, "//a[@href='/shoppingcart:cart.emptycart?nojs=1']")
# EMPTHY_CART_BTN_2 = (By.CSS_SELECTOR, "button.btn.btn-primary")
# EMPTHY_CART_BTN_2 = (By.XPATH, "//div[@class='modal-backdrop fade show']")

# open the url
driver.get( 'https://www.webstaurantstore.com/' )

# input search string
search = driver.find_element( By.ID, "searchval" )
search.clear()
search.send_keys( 'stainless work table' )

# click search
driver.find_element( By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn" ).click()

# verify all items with Table in the title are here
print( 'There are : ', len( driver.find_elements( By.CSS_SELECTOR, "input.btn.btn-cart.btn-small" ) ), 'items.' )

# add the last of found items to cart
driver.find_elements( By.CSS_SELECTOR, "input.btn.btn-cart.btn-small" )[-1].click()

# wait until pop-up desappears
sleep(10)

# click on cart button
driver.find_elements( By.CSS_SELECTOR, "span.menu-btn-text" )[1].click()

# click on cross symbol empty cart
driver.find_element( By.CSS_SELECTOR, "a.deleteCartItemButton.close" ).click()

# wait until cart is empthy
sleep(10)

# verify Your cart is empty
assert '0' in driver.find_element(By.ID, "cartItemCountSpan").text
print('Text in the cart button: ', str(driver.find_element(By.ID, "cartItemCountSpan").text), '.')

driver.quit()