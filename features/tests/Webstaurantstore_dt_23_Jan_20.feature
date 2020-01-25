# Created by rapid at 1/25/2020
Feature:
  1. Go to https://www.webstaurantstore.com/
  2.	Search for 'stainless work table'.
  3.	Check the search result ensuring every product item has the word 'Table' its title.
  4.	Add the last of found items to Cart.
  5.	Empty Cart.

  Scenario: User search, add, and delete item from the cart
    Given I am on Homepage
    Then Input item into search string
    Then Click search buton
    Then Verify all items with Table in the title are here
    Then Add the last of found items to cart
    Then Click on cart button
    Then Click on cross symbol empty cart
    Then Verify cart is empty



