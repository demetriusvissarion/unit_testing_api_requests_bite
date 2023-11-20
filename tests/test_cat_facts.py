import pytest
from lib.cat_facts import *
from unittest.mock import Mock


def test_calls_api_to_provide_cat_facts():
    requester_mock = Mock(name="requester") # This name is just for readability

    requester_mock.get().json.return_value = {'fact': 'Kittens remain with their mother till the age of 9 weeks.', 'length': 57}

    cat_facts = CatFacts(requester_mock)
    result = cat_facts.provide()
    assert result == 'Cat fact: Kittens remain with their mother till the age of 9 weeks.'