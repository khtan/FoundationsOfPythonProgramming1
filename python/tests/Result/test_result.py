""" Learning for Result """
# region imports
import logging
import sys
# import pytest
from expression import Error, Result, Ok
# endregion imports
# region globals
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(messag)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
# endregion globals
#region helpers
def even_only(n: int) -> Result[int, str]:
    """ Return Ok if n is even, else Error """
    if n % 2 == 0:
        return Ok(n)
    return Error(f"{n} is not even")
def log_result(res: Result[int, str]) -> None:
    """ Log the Result """
    if res.is_ok():
        # 1. Confirmed that after expression 2.2, the Result definition switched to T,Error instead of Error,T        
        # 2Q: how to extract Ok value?
        # The following while in various documentation do not work:
        # cresult.ok_value cresult.unwrap(), cresult.default_value, cresult.value
        # Found solution accidentally
        logger.info("Value is %d", res.ok)
    else:
        logger.error("Error: %s", res.error)
#endregion helpers
# region tests
# non symmetric: pytest.fail exists but not pytest.pass
# def test_01_xxx():
#    """ test_01_xxx """
#    pytest.fail("Test not implemented")

def test_02_fail():
    """ test_01_xxx """
    cresult = even_only(3)
    log_result(cresult)
def test_03_pass():
    """ test_01_xxx """
    cresult = even_only(4)
    log_result(cresult)
# endregion tests
