#imports
import sys
import logging
import pytest
logger = logging.getLogger(__name__)

# from pytest_mock import mocker
# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region tests
@pytest.mark.skip(reason="interactive test")
def test_input_nameA():
    person = input('Enter your name: ')
    print('Hello {}!'.format(person))

def test_input_name2A(mocker):
       new_mocker = mocker.patch('builtins.input', return_value='Alviso')
       person = input('Enter your name: ')
       logger.info('Hello {}!'.format(person))
# endregion tests
# main
# test_input_name2(mocker) # this fails bec don't know where mocker lives

