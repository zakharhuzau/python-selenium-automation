# Created by Zakhar at 10/1/2022
Feature: Test Scenarios for BestSellers page and the cart page
  # Enter feature description here

  Scenario: Verify: BestSeller page are 5 links
    Given Open BestSeller page
    Then Verify there are 5 links


  Scenario:  Add any product into the cart
    Given Open Amazon page
    When Input toys into Amazon search field
    And Click on search button
    And Click on any product
    And Click on add to cart button
    Then Verify Amazon Cart(1)
