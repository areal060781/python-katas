import pytest
import json

from config import basedir
from hackerrank.bigger_is_greater import bigger_is_greater as big

tc = basedir.joinpath('static', 'test_cases.json')


def load_tc_from_file(tc_params, tc_file):
    params = [x.strip() for x in tc_params.split(',')]

    def wrapper(function):
        with open(tc_file) as f:
            tc_data = json.loads(f.read())
        tc_cases = [tuple((case[p] for p in params)) for case in tc_data]
        function.tc_cases = tc_cases
        function.tc_params = tc_params

        return function

    return wrapper


def pytest_generate_tests(metafunc):
    if getattr(metafunc.function, 'tc_cases', None):
        metafunc.parametrize(metafunc.function.tc_params, metafunc.function.tc_cases)


@load_tc_from_file('test_input, expected', tc.absolute())
def test_eval(test_input, expected):
    assert big(test_input) == expected
