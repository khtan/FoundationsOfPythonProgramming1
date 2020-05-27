# region imports
import os
import sys
import logging
import pytest
import io

''' Notes
1. 
2.
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers
# endregion helpers
# region tests for xx.x
def test_1921_indexerror(): # 19.2.1
    items = ['a', 'b']
    with pytest.raises(IndexError):
        third = items[2]

def test_1921_zerodivisionerror(): # 19.2.1
    x = 5
    with pytest.raises(ZeroDivisionError):
        y = 5/0

def test_1921_trycatch():
    try:
        items = ['a','b']
        third = items[2]
        logger.info("This line will not print")
    except Exception as e:
        logger.info("Got an error")
        logger.info(e)

def test_1951_question():
    ''' The code below assigns the 5th letter of each word in food to the new list fifth. 
    However, the code currently produces errors. 
    Insert a try/except clause that will allow the code to run and produce of list of the 5th letter in each word. 
    If the word is not long enough, it should not print anything out. 
    Note: The pass statement is a null operation; nothing will happen when it executes.

    ? Did not need try/except nor pass statement
    '''
    food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
    fifth = []

    for x in food:
        if len(x)>= 5:
            fifth.append(x[4])

    logger.info(fifth)    
# endregion tests
