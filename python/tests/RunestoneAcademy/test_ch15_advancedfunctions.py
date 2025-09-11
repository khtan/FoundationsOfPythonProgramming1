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
def test_15211_keyword_format(): # 15.2.1
    names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
    for name, scores in names_scores:
        logger.info("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))

def test_15212_keyword_format(): # 15.2.1
    names = ["Jack","Jill","Mary"]
    # this works    
    for n in names:
        logger.info("A: '{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))
    for n in names:
        logger.info("B: '{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

def f(x):
    return x - 1

def test_1531_lambda(): # 15.3
    logger.info(f)
    logger.info(type(f))
    logger.info(f(3))

    logger.info(lambda x: x-2)
    logger.info(type(lambda x: x-2))
    logger.info((lambda x: x-2)(6))


# endregion tests
