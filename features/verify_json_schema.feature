Feature: Verify json schemas
  I want to get predictable response, that contain data, that I need to get

  Scenario: Validate blockchain principles for first and second blocks for one node
    When I request first block from prod node
    Then I should get successful response
    And  Response data should be like in get_blocks json schema

  Scenario: Validate JSON schema for heading block
    When I request global properties from prod node
    And I remember head block number and head block id
    When I request heading block from prod node
    Then I should get successful response
    And  Response data should be like in get_blocks json schema

  Scenario: Validate JSON schema for global properties
    When I request global properties from prod node
    Then I should get successful response
    And  Response data should be like in get_dynamic_global_properties json schema