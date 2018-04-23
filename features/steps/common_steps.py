import time
from behave import given, step, then, when
from nose.tools import assert_is_not_none, assert_in, assert_equal, assert_true

from helpers.converter import convert_from_string
from helpers.json_validator import validate_schema
from helpers.soft_assert import soft_assert


@then('I should receive error message "{message}"')
def step_impl(context, message):
    error = context.response.json().get('error')
    assert_is_not_none(error)
    assert_in(str(error['code']), context.errorCodesParser.get_code_for_message(message))
    soft_assert(message, error['message'])


@then('return error: "{error_message}"')
def step_impl(context, error_message):
    assert_equal(error_message, context.response.json()['error']['message'])


@step('details: "{details}"')
def step_impl(context, details):
    soft_assert(details, context.response.json()['error']['details'])


@step('fail with {message}')
def step_impl(context, message):
    raise Exception('Test fail: %s' % message)


@step('Response should have {composite_key:w} = {value}')
def step_impl(context, composite_key, value):
    response = context.response.json()
    for key in composite_key.split('.'):
        response = response[key]

    try:
        value = int(value)
    except ValueError:
        if value == '{TestData}':
            value = context.test_data[composite_key.split('.')[-1]]
        else:
            convert_from_string(context, value)

    assert_equal(response, value)


@then('I should get successful response with no content')
def step_impl(context):
    assert_equal(203, context.response.status_code)


@then('I should get successful response')
def step_impl(context):
    assert_equal(200, context.response.status_code)


@then('I should get {code} status code in response')
def step_impl(context, code):
    assert_equal(code, context.response.status_code)


@step('Response should have {key}: "{value}"')
def step_impl(context, key, value):
    assert_equal(convert_from_string(context, value), context.response.json()[key])


@when("I send {request_name} request")
def step_impl(context, request_name):
    request_name = str(request_name).replace(" ", "_")
    context.response = context.api.__getattribute__(request_name)()


@step("Response should not be empty")
def step_impl(context):
    assert_true(len(context.response.json()) > 0)


@step("Response should have list {list_name} with {element_name}")
def step_impl(context, list_name, element_name):
    response = context.response.json()
    assert_true(response[list_name])
    for element in response[list_name]:
        assert_true(element[element_name])


@step("Response data should be like in {json_schema_name} json schema")
def step_impl(context, json_schema_name):
    validate_schema(context.response.json(), json_schema_name)


@step("I wait for {seconds} seconds")
def step_impl(context, seconds):
    time.sleep(int(seconds))
