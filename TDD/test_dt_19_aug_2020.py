from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

SEARCH_STRING = (By.ID, "searchval")
SEARCH_BTN = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
ITEMS_DESCRIPTIONS = (By.CSS_SELECTOR, "a.description")
ITEMS_TO_CHOOSE = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
PRODUCTS = (By.CSS_SELECTOR, '.ag-item.gtm-product')
CART_BTN = (By.NAME, "cart")
EMPTY_CROSS_SIGN = (By.CSS_SELECTOR, "a.deleteCartItemButton.close")
CART_ITEM = (By.ID, "cartItemCountSpan")

# I am on Homepage
driver.get( 'https://www.webstaurantstore.com/' )


# Input item into search string
search = driver.find_element(*SEARCH_STRING)
search.clear()
search.send_keys('stainless work table')


# Click search button
driver.find_element(*SEARCH_BTN).click()


# Verify all items with Table in the title are here
print('There are : ', len(driver.find_elements( *ITEMS_TO_CHOOSE )), 'items.')
print('There are : ', len(driver.find_elements( *ITEMS_DESCRIPTIONS)), 'descriptions.')
products = driver.find_elements( *PRODUCTS )
for product in list(products):
    title = product.find_element( *ITEMS_DESCRIPTIONS )
print('Title:', title.text, '.')
assert 'Table' in title.text


# Add the last of found items to cart
sleep(8)
# target = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
# actions = ActionChains(driver)
# actions.move_to_element(target)
# sleep(2)
# actions.click(target)
# actions.perform()
driver.find_elements( *ITEMS_TO_CHOOSE )[-1].click()
# wait until pop-up desappears
sleep(8)


# Click on cart button
# target = driver.find_element(By.NAME, "cart")
# actions = ActionChains(driver)
# actions.move_to_element(target)
# sleep(2)
# actions.click(target)
# actions.perform()
driver.find_element( *CART_BTN ).click()
sleep(8)


# Click on cross symbol empty cart
# target = driver.find_element(By.CSS_SELECTOR, "a.deleteCartItemButton.close")
# actions = ActionChains(driver)
# actions.move_to_element(target)
# sleep(2)
# actions.click(target)
# actions.perform()
driver.find_element( *EMPTY_CROSS_SIGN ).click()
# wait until cart is empthy
sleep(4)


# Verify cart is empty
print('Text in the cart button: ', str(driver.find_element( *CART_ITEM ).text),'.')

# Exit
driver.quit()