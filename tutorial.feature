

Feature: Automation test dogs

  Scenario: Happy path automation
     When  I request GET
      Then I should receive an OK  response
      And I check that response contains property "message" is akita
      


      