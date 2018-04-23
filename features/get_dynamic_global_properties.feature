Feature: Validate get_dynamic_global_properties endpoint

  Scenario: Validate blocks generation in one node
    When I request global properties from prod node
    And I remember head block number and head block id
    And I wait for 3 seconds
    When I request global properties from prod node
    Then I validate that heading block id and heading block number are changed


  Scenario: Validate blocks generation between nodes
    When I request global properties from node1 node
    And I remember head block number and head block id
    And I wait for 3 seconds
    When I request global properties from node2 node
    Then I validate that heading block id and heading block number are changed


  Scenario: Validate global properties between nodes
    When I request global properties from node1 node
    And I remember head block number and head block id
    When I request global properties from node2 node
    Then I validate that heading block id and heading block number are the same