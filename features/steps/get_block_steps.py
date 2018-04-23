from behave import when, given, then
from nose.tools import assert_equals, assert_not_equals, assert_true

from helpers.converter import convert_from_string


@when("I request {block_id} block from {node} node")
@given("I request {block_id} block from {node} node")
def step_impl(context, block_id, node):
    context.test_data['block_id'] = convert_from_string(context, block_id)
    context.response = context.api[node].get_blocks(**context.test_data)
    context.responses[node][block_id] = context.response


@when("I request global properties from {node} node")
def step_impl(context, node):
    context.response = context.api[node].get_dynamic_global_properties()
    context.responses[node]['props'] = context.response


@when("I remember head block number and head block id")
def step_impl(context):
    context.additional_data['head_block_number'] = context.response.json()['result']['head_block_number']
    context.additional_data['head_block_id'] = context.response.json()['result']['head_block_id']


@then("I validate that {block_id_last} block from {node_last} node is connected to {block_id_first} block from {node_first} node")
def step_impl(context, block_id_last, node_last, block_id_first, node_first):
    last_resp = context.responses[node_last][block_id_last].json()
    first_resp = context.responses[node_first][block_id_first].json()
    assert_equals(last_resp['result']['previous'], first_resp['result']['block_id'])
    assert_not_equals(last_resp['result']['block_id'], first_resp['result']['block_id'])
    assert_true(last_resp['result']['timestamp'] > first_resp['result']['timestamp'])
