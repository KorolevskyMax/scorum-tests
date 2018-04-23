Feature: Validate blockchain principles for get_block endpoint

  Scenario: Validate first and second blocks in one node
    Given I request first block from prod node
    When I request second block from prod node
    Then I validate that second block from prod node is connected to first block from prod node

  Scenario: Validate first and second blocks between nodes
    Given I request first block from node1 node
    When I request second block from node2 node
    Then I validate that second block from node2 node is connected to first block from node1 node

  Scenario: Validate 400000 and 400001 blocks in one node
    Given I request 400000 block from prod node
    When I request 400001 block from prod node
    Then I validate that 400001 block from prod node is connected to 400000 block from prod node

  Scenario: Validate heading and preheading blocks in one node
    When I request global properties from prod node
    And I remember head block number and head block id
    Given I request heading block from prod node
    When I request preheading block from prod node
    Then I validate that heading block from prod node is connected to preheading block from prod node

  Scenario: Validate heading and future blocks in one node
    When I request global properties from prod node
    And I remember head block number and head block id
    Given I request heading block from prod node
    And I wait for 3 seconds
    When I request future block from prod node
    Then I validate that future block from prod node is connected to heading block from prod node

  Scenario: Validate heading and future blocks between nodes
    When I request global properties from prod node
    And I remember head block number and head block id
    Given I request heading block from node1 node
    And I wait for 3 seconds
    When I request future block from node2 node
    Then I validate that future block from node2 node is connected to heading block from node1 node


  Scenario: Validate block generation
    When I request global properties from node2 node
    And I remember head block number and head block id
    And I request future block from node2 node
    Then Response should have result: "None"
    And I wait for 3 seconds
    When I request future block from node2 node
    And I request heading block from node1 node
    Then I validate that future block from node2 node is connected to heading block from node1 node
