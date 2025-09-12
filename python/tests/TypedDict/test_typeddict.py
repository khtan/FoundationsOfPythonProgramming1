""" Tests for TypedDict in Python 3.10+ """
# region imports
import sys
import logging
from typing import TypedDict

# pylint: disable=W0105
''' Notes
1. 
2.
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
# endregion globals
# region class
class Person(TypedDict):
    """ A simple TypedDict for a person """
    name: str
    age: int
    email: str | None

# endregion class
# region helpers
def log_person(user_data: Person) -> None:
    """ Print person details, function taking a Person type """
    logger.info("Processing %s, who is %d years old.", user_data['name'], user_data['age'])  
# endregion helpers
# region tests for xx.x
def test_01_person() -> None:
    """ Test creating and using a Person TypedDict """
    user1: Person = {"name": "Alice", "age": 30, "email": "alice@example.com"}
    log_person(user1)
    assert user1["name"] == "Alice"
# endregion tests
