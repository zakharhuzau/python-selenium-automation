# Created by Zakhar at 10/29/2022
Feature: Scenarios for using dropdown and hover

  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by value <department>
    And Input <product> into Amazon search field
    And Click on search button
    Then Verify <department> department is selected
    Examples:
      | department      | product |
      | amazon-devices  | ice     |
      | warehouse-deals | shirt   |

  Scenario: User can see the deals to hovers over New Arrivals
    Given Open Amazon product page gp/product/B074TBCSC8
    When Hovers over New Arrivals
    Then Verify user can see the deals