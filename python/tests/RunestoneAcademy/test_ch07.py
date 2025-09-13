""" Tests for chapter 7 of Runestone Academy book Foundations of Python Programming 1 """
#imports
import logging

# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers
def reverse_string(input_string):
    """ Return the reverse of the input string """
    return input_string[::-1]

def query_string(capsys, input_values, expected_output): # pylint: disable=W0613
    """ Simulate input and capture output for testing """
    def mock_input(s):
        print(s, end='')
        val = input_values.pop(0)
        logger.info("input: %s", val)
        return val

    input_1 = mock_input
    text=input_1("Enter a string:")
    reverse = reverse_string(text)
    logger.info("rev: %s", reverse)
    assert reverse == expected_output

# endregion helpers
# region tests
def test_ducklings2():
    """ Test for ducklings2 """
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for pre in prefixes:
        logger.info("%s%s", pre, suffix)

def test_ducklings():
    """ Test for ducklings """
    first_chars = ['J','K','L','M','N','O','P','Q']
    for first in first_chars:
        logger.info("%sack", first)

def test_reverse(capsys):
    """ Test for reverse string """
    query_string(capsys, ["hello world"], "dlrow olleh")


def test_months():
    """ Test for months of the year """
    months = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September","October","November", "December"]
    for month in months:
        logger.info("One of the months of the year is %s", month)

# endregion tests
