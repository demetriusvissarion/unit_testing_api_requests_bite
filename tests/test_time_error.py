import pytest
from lib.time_error import *
from unittest.mock import Mock


def test_calls_api_to_provide_time():
    requests_mock = Mock(name="requests") # This name is just for readability
    response_mock = Mock(name="response")
    time_mock = 1700485279.628256

    requests_mock.get.return_value = response_mock

    # We tell `response_mock` to return a sample output of the API when
    # we call `json()` on it.
    # I got this sample using `curl "https://www.boredapi.com/api/activity"`.
    response_mock.json.return_value = {'abbreviation': 'GMT', 'client_ip': '82.163.117.26', 'datetime': '2023-11-20T13:01:19.684576+00:00', 'day_of_week': 1, 'day_of_year': 324, 'dst': False, 'dst_from': None, 'dst_offset': 0, 'dst_until': None, 'raw_offset': 0, 'timezone': 'Europe/London', 'unixtime': 1700485279, 'utc_datetime': '2023-11-20T13:01:19.684576+00:00', 'utc_offset': '+00:00', 'week_number': 47}

    time_error = TimeError(requests_mock, time_mock)
    result = time_error.error()
    assert result == -0.62825608253479