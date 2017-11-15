Feature: New Gmail account creation Form
  In order to create a new user, a registry form should be filled. This Form is validated and if all data it is ok the next step screen is loaded

  Scenario: User is able to create a gmail account
    Given The registry form loaded
    When User set Roberto on FirstName field
      And User set Mangos on LastName field
      And User set myPersonalEmail on Choose your username field
      And User set myPassword on Confirm your password field
      And User seelect April option on Month combobox
      And User set 16 on Day field
      And User set 1980 on Year field
      And User select Male option on Gender combobox
      And User set otherEmail@mail.com on your current email addres field
      And User press on Next button
    Then All data intoduced in the form is validated
    And The next screen is loaded


