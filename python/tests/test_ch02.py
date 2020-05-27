#imports
import sys
import logging
from pytest import approx
# globals
logger = logging.getLogger(__name__)

# pure functions
# Compute the day of week given start day and length of day interval
def dayofweek(start:int, length:int) -> int:
    return (start + length) % 7

# Compute compound interest
def compound_interest(principal: int, num: int, rate: float, years:int ):
    return principal * ( (1 + (rate/num)) ** (num * years))

# impure convenience test functions
# These 2 query_ functions illustrate that for robust and maintenable tests, these should be
# refactored as well, so that the mock_input <-> input_values <-> input_types can be formalized
# This function uses capsys to check input and outputs
def query_dayofweek(capsys, input_values, expected_output):
    def mock_input(s):
        print(s, end='')
        return input_values.pop(0)
    input = mock_input
    smsg = "Please enter the starting day number: "
    lmsg = "Please enter the length of stay: "
    s = int(input(smsg))
    l = int(input(lmsg))
    r = dayofweek(s,l)
    logger.info(r)
    assert r == expected_output
    outmsg, err = capsys.readouterr()
    assert outmsg == (smsg + lmsg)
    assert 0 == len(err)

# ?
def query_compound_interest(capsys, principal, num, rate, input_values, expected_output):
    def mock_input(s):
        print(s, end='')
        return input_values.pop(0)
    input = mock_input
    yearsmsg = "Please enter compound for how many years: "
    years = int(input(yearsmsg))
    final = compound_interest(principal, num, rate, years)
    logger.info(final)
    assert final == approx(expected_output)
    outmsg, err = capsys.readouterr()
    assert outmsg == yearsmsg
    assert 0 == len(err)

# tests
# Q5: Challenge: Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.
def test_allwork(capsys):
    a='All'
    b='work'
    c='and'
    d='no'
    e='play'
    f='makes'
    g='Jack'
    h='a'
    i='dull'
    j='boy'
    print(a,b,c,d,e,f,g,h,i,j)
    out, err = capsys.readouterr()
    expected_output = a + ' ' + b + ' ' + c + ' ' + d + ' ' + e + ' ' + f + ' ' + g + ' ' + h + ' ' + i + ' ' + j + '\n'
    logger.info('out: ' + out)
    assert out == expected_output
    assert 0 == len(err)

# Q4: It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
def test_dayofweek(capsys):
    input_values = [3, 10]
    query_dayofweek(capsys, input_values, 6)

# Q7: Challenge: The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
#     A = P ( 1 + r/n )** nt
# Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
def test_compound_interest(capsys):
   input_values = [10]
   query_compound_interest(capsys, 10000, 12, 0.08, input_values, 22196.4023454)
