""" Tests for TypedDict in Python 3.10+ """
# region imports
import os
import sys
import logging
import json
from typing import TypedDict
from expression import Error, Result, Ok

import pytest

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
def load_json_file(file_path: str) -> Person:
    """ Load a JSON file and return a Person """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        json_str = json.dumps(data)
        user: Person = json.loads(json_str, object_hook=Person) # type: ignore
    return user
def safe_load_json_file(file_path: str) -> Result[Person, str]:
    """ Load a JSON file and return a Person TypedDict """
    if not os.path.exists(file_path):
        return Error("File {file_path} not found")

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            json_str = json.dumps(data)
            user: Person = json.loads(json_str, object_hook=Person) # type: ignore
            return Ok(user)
        except json.JSONDecodeError as e:
            return Error(f"Failed to parse JSON from {file_path}: {e}")
        # Break broad-except for FP style
        except Exception as e: # pylint: disable=broad-except
            return Error(f"Unexpected error occurred while loading {file_path}: {e}")

# endregion helpers
# region tests for xx.x
def test_01_create_person() -> None:
    """ Test creating and using a Person TypedDict """
    user1: Person = {"name": "Alice", "age": 30, "email": "alice@example.com"}
    log_person(user1)
    assert user1["name"] == "Alice"
def test_02_read_config_file() -> None:
    """ Test creating and using a Person TypedDict from config file"""
    config_file_name = "test_typeddict_config.txt"
    base_dir = os.path.dirname(__file__)
    config_file = os.path.join(base_dir, config_file_name)
    user1: Person = load_json_file(config_file)
    logger.info("Loaded user: %s", user1)
    log_person(user1)
    assert user1["name"] == "John"
def test_03_exception_file_does_not_exist() -> None:
    """ Test file-does-not-exist"""
    config_file_name = "file_does_not_exist.txt"
    base_dir = os.path.dirname(__file__)
    config_file = os.path.join(base_dir, config_file_name)
    with pytest.raises(FileNotFoundError):
        unused_person: Person = load_json_file(config_file) # pylint: disable=W0612
def test_04_result_file_does_not_exist() -> None:
    """ Test file-does-not-exist"""
    config_file_name = "file_does_not_exist.txt"
    base_dir = os.path.dirname(__file__)
    config_file = os.path.join(base_dir, config_file_name)
    cresult = safe_load_json_file(config_file)
    if cresult.is_ok():
        pytest.fail("Expected an error due to missing file")
    else:
        assert "not found" in str(cresult.error)
# endregion tests
