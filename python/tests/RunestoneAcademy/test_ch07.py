#imports
import sys
import logging
import pytest

# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers
def reverse_string(input_string):
    return input_string[::-1]

def query_string(capsys, input_values, expected_output):
    def mock_input(s):
        print(s, end='')
        val = input_values.pop(0)
        logger.info("input: " +val)
        return val
    input = mock_input
    text=input("Enter a string:")
    reverse = reverse_string(text)
    logger.info("rev: " + reverse)    
    assert reverse == expected_output

# endregion helpers
# region tests
def test_ducklings2():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for pre in prefixes:
        logger.info(pre + suffix)

def test_ducklings():
    firstChars = ['J','K','L','M','N','O','P','Q']
    for first in firstChars:
        logger.info(first + 'ack')

def test_reverse(capsys):
    query_string(capsys, ["hello world"], "dlrow olleh")


def test_months():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October","November", "December"]
    for month in months:
        logger.info("One of the months of the year is " + month)

# endregion tests
