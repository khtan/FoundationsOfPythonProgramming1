# region imports
import os
import sys
import logging
import pytest
import io

''' Notes
1. slice is sequence[start:stop:step]
Both start and stop are indices, not count
Overindexing does not cause problems, the rest still works as expected
2.
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
tlst1 = ['b', 'c', 'd']
epost = ['b', 'c','d','e'] # expected list after postpend
epre  = ['a', 'b', 'c','d'] # expected list after prepend
# endregion globals
# region helpers
# endregion helpers
# region tests for xx.x
# list[3:x] where x = empty, 0,
def test_01_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:] = 'e' # second index is default to the end
    logger.info(lst)
    assert epost == lst
def test_02_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:-3] = 'e' # slice from back, should work
    logger.info(lst)
    assert epost == lst
def test_03_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:-2] = 'e' # slice from back, should work
    logger.info(lst)
    assert epost == lst
def test_04_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:-1] = 'e' # -1 is valid
    logger.info(lst)
    assert epost == lst
def test_05_postpend_frontindex():
    lst = tlst1.copy()
    # list[3] = 'd' # this fails bec list is overindexed
    lst[3:0] = 'e' # slice from front, 0 is not valid
    logger.info(lst)
    assert epost == lst
'''
    list[4:1] = 'e' # slice from front, should also work
    logger.info(list)
    list[5:2]='f' # overslice
    logger.info(list)
'''
def test_06_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:1] = 'e' # -1 is valid
    logger.info(lst)
    assert epost == lst
def test_07_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:2] = 'e' # -1 is valid
    logger.info(lst)
    assert epost == lst
def test_08_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:3] = 'e' # slice from front, 3 is not valid
    logger.info(lst)
    assert epost == lst
def test_09_postpend_frontindex():
    lst = tlst1.copy()
    lst[3:4] = 'e' # 4 is invalid
    logger.info(lst)
    assert epost == lst
def test_01_prepend_frontindex():
    lst = tlst1.copy()
    lst[:0] = 'a'
    logger.info(lst)
    assert epre == lst
def test_02_prepend_frontindex():
    lst = tlst1.copy()
    lst[:0:1] = 'a'
    logger.info(lst)
    assert epre == lst
def test_03_prepend_frontindex():
    lst = tlst1.copy()
    with pytest.raises(ValueError):
        lst[:0:2] = 'a'
# endregion tests
