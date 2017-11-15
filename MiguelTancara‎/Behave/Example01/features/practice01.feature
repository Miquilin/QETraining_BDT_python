Feature: This is thw fisrt practice
  This is an example feature to start with the implementation of the steps

Scenario: First Scenario
  Given I have loaded the registry form
  When User set 12345 value on Zip Code field
  And User set Cochabamba value on Country code field
  And User set 987645 on Number Habitats field
  And User press on Save button
  Then User is saved on BD