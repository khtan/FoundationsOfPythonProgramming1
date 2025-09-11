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
# region tests
def stop_at_four(lst):
    nlist = []
    count = 0
    while ((count < len(lst)) and (lst[count] != 4)): # guard against overindexing recommended
        nlist.append(lst[count])
        count += 1
    return nlist
def test_1421_stop_at_four():
    ''' Write a function called stop_at_four that iterates through a list of numbers. 
    Using a while loop, append each number to a new list until the number 4 appears. 
    The function should return the new list.
    '''
    list1 = [0,9,4.5,1,7,4,8,9,3]
    logger.info(stop_at_four(list1))

def test_can_for_have_break(): # answer is yes
    for x in range(5):
        if x == 3: break
        logger.info(x)

# endregion tests
