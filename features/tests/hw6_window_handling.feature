# Created by Zakhar at 10/18/2022
Feature: Test Scenarios for handling test case and test case using a loop

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original

  Scenario: Clicks on each top link and verifies that correct page opens
    Given Open Amazon page
    When Click on Best Sellers link
    Then Clicks on each top links and verifies these