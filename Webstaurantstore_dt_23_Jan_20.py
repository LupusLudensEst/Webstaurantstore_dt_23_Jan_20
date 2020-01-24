from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

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
print( 'There are 1: ', len( driver.find_elements( By.CSS_SELECTOR, "a.description" ) ), 'items' )
print( 'There are 2: ', len( driver.find_elements( By.CSS_SELECTOR, "input.btn.btn-cart.btn-small" ) ), 'items' )

# add the last of found items to cart
driver.find_elements( By.CSS_SELECTOR, "input.btn.btn-cart.btn-small" )[-1].click()
driver.find_elements( By.CSS_SELECTOR, "a.menu-btn" )[1].click()
driver.find_element( By.XPATH, "//a[@href='/shoppingcart:cart.emptycart?nojs=1']" ).click()
try:
    driver.find_element(By.XPATH, "//div[@class='modal-backdrop fade show']").click()
except ElementClickInterceptedException:
    driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary")[4].click()

sleep(20)

driver.quit()