from behave import *
from nose.tools import assert_equals, assert_not_equals


@then("I validate that heading block id and heading block number are changed")
def step_impl(context):
    assert_equals(context.response.json()['result']['head_block_number'], context.additional_data['head_block_number'] + 1)
    assert_not_equals(context.response.json()['result']['head_block_id'], context.additional_data['head_block_id'])


@then("I validate that heading block id and heading block number are the same")
def step_impl(context):
    assert_equals(context.response.json()['result']['head_block_number'], context.additional_data['head_block_number'])
    assert_equals(context.response.json()['result']['head_block_id'], context.additional_data['head_block_id'])
