# Created by Zakhar at 9/29/2022
Feature: Test Scenarios for Sign In page
  # Enter feature description here

  Scenario: Verify Sign In page
    Given Open Amazon page
    When Click orders
    Then Verify: Sign In header is visible and email input field is present
    # Enter steps here