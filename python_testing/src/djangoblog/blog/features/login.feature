Feature: Login
  In order to have unlimited powers
  As a system anonymous user
  I want to login in the system

  Scenario Outline: The admin page is served without error
    When I navigate to the login page
    Then I see the header 'Django administration'
