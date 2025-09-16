""" Tests for TypedDict in Python 3.10+ """
# region imports
import sys
import logging
# from typing import TypedDict
from expression import Error, Result, Ok

# import pytest

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
errstr = str # reminder for error strings # pylint: disable=invalid-name
# endregion globals
# region helpers
def get_hexagram_unicode(hexagram_number: int) -> Result[str, errstr]:
    """ Get the Unicode character for a given hexagram number (1-64) """
    if 1 <= hexagram_number <= 64:
        return Ok(chr(0x4DC0 + hexagram_number - 1))
    else:
        return Error("Hexagram number must be between 1 and 64")

def get_trigram_unicode(trigram_number: int) -> Result[str, errstr]:
    """ Get the Unicode character for a given trigram number (1-8) """
    if 0 <= trigram_number <= 7:
        return Ok(chr(0x2630 - trigram_number + 7))
    else:
        return Error("Trigram number must be between 0 and 7")
# endregion helpers
# region test helpers
def show_results(res: Result[str, errstr]) -> None:
    """ Show the result """
    if res.is_ok():
        logger.info("Result: %s", res.ok)
    else:
        logger.error("Error: %s", res.error)
# end region test helpers
# region tests
def test_01_valid_hexagram() -> None:
    """ Test  """
    hexagram_number = 1
    result = get_hexagram_unicode(hexagram_number)
    show_results(result)
def test_01_valid_trigram() -> None:
    """ Test  """    
    trigram_number = 0
    result = get_trigram_unicode(trigram_number)
    show_results(result)
def test_02_invalid_hexagram() -> None:
    """ Test  """
    hexagram_number = 0
    result = get_hexagram_unicode(hexagram_number)
    show_results(result)
def test_02_invalid_trigram() -> None:
    """ Test  """    
    trigram_number = 8
    result = get_trigram_unicode(trigram_number)
    show_results(result)

# endregion tests
