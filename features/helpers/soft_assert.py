__author__ = 'Max'
import sys

from nose.tools import assert_equal


def soft_assert(first, second, assert_type=assert_equal):
    try:
        assert_type(first, second)
    except AssertionError:
        _, value, _ = sys.exc_info()
        print("Assertion error: {assertion_error_message}".format(assertion_error_message=value))
