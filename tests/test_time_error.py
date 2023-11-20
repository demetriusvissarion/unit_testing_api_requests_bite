import pytest
from lib.time_error import *
from unittest.mock import Mock


def test_calls_api_to_provide_time():
    requests_mock = Mock(name="requests") # This name is just for readability
    response_mock = Mock(name="response")

    # We tell `requester_mock` to return `response_mock` 
    # when we call `get()` on it.
    requests_mock.get.return_value = response_mock

    # We tell `response_mock` to return a sample output of the API when
    # we call `json()` on it.
    # I got this sample using `curl "https://www.boredapi.com/api/activity"`.
    response_mock.json.return_value = {
        
    }

    time_error = TimeError(requests_mock)
    result = time_error.error()
    assert result == ""