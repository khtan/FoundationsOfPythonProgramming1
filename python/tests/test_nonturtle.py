#imports
import sys
import logging
import pytest
import random
# region globals
logger = logging.getLogger(__name__)

# endregion globals
# pure functions
# region impure
def setup_function():
   logger.info("setup_method")

def teardown_function():
   logger.info("teardown_method")

# endregion impure
# region tests
# currently may be more complicated to inject mock_input and verify array of 100 lines
def test_1_weliketurtles():
    for _ in range(100):
        logger.info("We like Python's turtles")

# Use a for statement to print 10 random numbers.
def test_2_random():
   for _ in range(10):
      logger.info(random.random())

# Repeat the above exercise but this time print 10 random numbers between 25 and 35.
def test_3_randrange():
   for _ in range(10):
      logger.info(random.randrange(25,35+1))

# endregion tests

