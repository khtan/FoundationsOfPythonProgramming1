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
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
# endregion globals
# region helpers
# endregion helpers
# region tests for xx.x
def test_01_surprising_pattern():
    for i in range(1, 10): # start=1, excludestop=10, range does not take parameter name
        istr = str(1)*i
        inum = int(istr)
        logger.info("{:>9} * {:9} = {:^18}".format(istr, istr, inum * inum))

# endregion tests
