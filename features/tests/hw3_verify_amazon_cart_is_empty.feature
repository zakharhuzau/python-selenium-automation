# Created by Zakhar at 9/30/2022
Feature: Test Scenarios for Amazon Cart

  Scenario: Verify Amazon Cart
    Given Open Amazon page
    When Click Cart
    Then Verify Amazon Cart(0)