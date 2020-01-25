# Created by rapid at 1/25/2020
Feature: User deletes item from cart

  Scenario: User search, add, and delete item from the cart
    Given I am on Homepage
    Then Input item into search string
    Then Click search button
    Then Verify all items with Table in the title are here
    Then Add the last of found items to cart
    Then Click on cart button
    Then Click on cross symbol empty cart
    Then Verify cart is empty