# region imports
import os
import sys
import logging
import pytest
import io
import functools

''' Notes
1. In Python, the object ( List) has a class function called sort. This mutates the object itself.
2. There is also a global method Sorted that creates a copy of the object before sorting.
3. sorted takes either a cmp function or a key function
   int cmp(ele1, ele2) where return is negative, zero or positive as to <, ==, >
   comparison-key key(ele)
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers
# endregion helpers
# region tests for xx.x
def test_1611_sort_is_mutable(): # 16.1
    L1 = [1, 7, 4, -2, 3]
    L2 = ["Cherry", "Apple", "Blueberry"]

    L1.sort()
    logger.info(L1)
    sortedL1 =  [-2, 1, 3, 4, 7]
    assert sortedL1 == L1
    L2.sort()
    logger.info(L2)
    sortedL2 = ['Apple', 'Blueberry', 'Cherry']
    assert sortedL2 == L2

def test_1621_reverse_parameter():
    L1 = ['c','a','b']
    sortedreverseFalseL1 = sorted(L1)
    sortedreverseTrueL1 = sorted(L1, reverse=True)
    logger.info(sortedreverseFalseL1)
    logger.info(sortedreverseTrueL1)
    esortedreverseFalseL1 = ['a','b','c']
    esortedreverseTrueL1 = ['c','b','a']
    assert esortedreverseFalseL1 == sortedreverseFalseL1
    assert esortedreverseTrueL1 == sortedreverseTrueL1

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

def test_1631_key_parameter():
    L1 = [1, 7, 4, -2, 3]
    L2 = sorted(L1, key=absolute)
    eL2 = [1, -2, 3, 4, 7]
    logger.info(L2)
    assert eL2 == L2
def test_1631b_key_parameter():
    L1 = [1, 7, 4, -2, 3]
    L2 = sorted(L1, key=lambda x: abs(x))
    eL2 = [1, -2, 3, 4, 7]
    logger.info(L2)
    assert eL2 == L2

def test_1631_cmp_parameter():
    ''' In Py3, cmp parameter is removed in favor of key parameter
        https://docs.python.org/3/howto/sorting.html#sortinghowto    

        The documentation in https://python-reference.readthedocs.io/en/latest/docs/functions/sorted.html is
        incorrect or only for Py2. It shows signature as sorted(iterable, cmp[, key[,reverse]])

        Similarly, in https://docs.python.org/3/library/functions.html#sorted, signature of sorted
        is sorted(iterable, *, key=None, reverse=False) where the extra * is not necessary/correct
    '''
    L1 = [1, 7, 4, -2, 3]
    L2 = sorted(L1, key=functools.cmp_to_key(lambda x,y: abs(x) - abs(y)))
    eL2 = [1, -2, 3, 4, 7]
    logger.info(L2)
    assert eL2 == L2

def test_1641_sort_keys_dictionary():
    d = {"E": 2, "F": 1, "B": 2, "A":2, "D":4, "I": 2, "C":1}
    for k in sorted(d.keys()):
        logger.info("{} -> {}".format(k, d[k]))

def test_1641_sort_count_dictionary():
    d = {"E": 2, "F": 1, "B": 2, "A":2, "D":4, "I": 2, "C":1}
    for k in sorted(d.keys(), key=lambda k: d[k], reverse=True):
        logger.info("{} -> {}".format(k, d[k]))

def test_1651_sort_count_with_ties_dictionary():
    ''' Using tuple for secondary sort, but the reverse applies both times
        so -d[k] is required to get sort output. This shows the interaction between key and reverse
        can get messy
    '''
    d = {"E": 2, "F": 1, "B": 2, "A":2, "D":4, "I": 2, "C":1}
    for k in sorted(d.keys(), key=lambda k: (-d[k], k), reverse=False):
        logger.info("{} -> {}".format(k, (d[k])))

def sort_dictionary(inputD, sortFn):
    return sorted(inputD.items(), key = sortFn)

def string_cmp(a,b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def reverse_string_cmp(a,b):
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0
def test_sort_dictionary():
    orders = { 
    'latte': 48,
    'espresso': 54,
    'americano': 48,
    'cortado': 41,
    'cappucino': 54
    }
    # x[0] is the key, x[1] is the value
    sort1 = sorted(orders.items(), key = lambda item: (item[1], item[0]))
    logger.info("sort1: {}".format(sort1))
    sort2 = sorted(orders.items(), key = lambda item: orders[item[0]])
    logger.info("sort2: {}".format(sort2))
    sort3 = sort_dictionary(orders, lambda item: item[1])
    logger.info("sort3: {}".format(sort3))

def test_reverse_sort_strings():
    # https://stackoverflow.com/questions/55866762/how-to-sort-a-list-of-strings-in-reverse-order-without-using-reverse-true-parame
    listA = ['aaa', 'ccc', 'bbb']
    sortA = sorted(listA)
    sortB = sorted(listA, reverse=True)
    logger.info("sortA: {}".format(sortA))
    logger.info("sortB: {}".format(sortB))
    sortC = sorted(listA, key=functools.cmp_to_key(string_cmp))
    logger.info("sortC: {}".format(sortC))
    sortD = sorted(listA, key=functools.cmp_to_key(reverse_string_cmp))
    logger.info("sortD: {}".format(sortD))
# endregion tests
