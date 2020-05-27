# region imports
import os
import sys
import logging
import pytest
import io
import math

''' Notes Ch13 Tuples
1. When a single value is expected, multiple expressions separated by commas will be automatically packed into a tuple. The parenthesis can be omitted.
   This applies in both directions of assignment
   (x,y) = areaOfCircle(r) or x,y = areaOfCircle(r)
   # printTuple(x,y) no, printTuple((x,y)) yes
2. Tuple assignment supports direct swapping, (a,b) = (b,a)
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers
def add(x,y):
    return x + y

def circleInfo(r):
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a # or return (c,a)

# endregion helpers
# region tests for xx.x
def test_1300_simple():
    s = "bob"
    n = 23
    t = (s,n)
    logger.info("tuple[0]={}, tuple[1]={}".format(t[0], t[1]))
    assert s == t[0]
    assert n == t[1]
def test_1321_autopacking():
    julia1 = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
    # or equivalently
    julia2 = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
    logger.info("julia1[4]={}".format(julia1[4]))
    assert julia1[4] == julia2[4]

def test_1322_creation():
    practice = 'y', 'h', 'z', 'x'
    assert 4 == len(practice)

def test_1323_tupleindex(): # tuple integer indices works as expected
    julia1 = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
    assert "Atlanta, Georgia" == julia1[-1] # last item can be indexed from behind

def test_1324_iterate_tuple_list():
   ''' Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
       C#: Creating a list of different tuples is messy
   '''
   lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
   t_check = []
   for t in lst_tups:
       t_check.append(t[2])
   logger.info(t_check)
   assert ['Zaptos', 'Charizard', 'Diglett', 'Tauros', 'Lanturn', 'Wailord'] == t_check

def test_1325_iterate_mixedtuples_list():
    ''' Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.
    '''
    tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
    seconds = []
    for t in tups:
        # seconds[0:] = t[1] // this does not work, TypeError: can only assign an iterable
        seconds.append(t[1])
    logger.info(seconds)
    assert ['b', 7, 'green', 9.99, 'chipmunk'] == seconds
def test_1330_unpack():
    julia1 = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
    name, surname, birth_year, movie, movie_year, profession, birth_place = julia1
    assert "Julia" == name
    assert 2009 == movie_year

def test_1331_swap(): # 13.3.1
   a = "hello"
   b = 123
   (a,b) = (b,a)
   assert "hello" == b
   assert 123 == a
def test_1332_unpack_into_iterator():
    authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
    for first_name, last_name in authors:
        logger.info("first name: {}, last name: {}".format(first_name, last_name))

  
def test_1333_enumerate(): # 13.3.3
    ''' 1. enumerate can only be run once
        2. the list() has to re-enumerate
    '''
    fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
    efruits = enumerate(fruits)
    for item in efruits:
        logger.info("{} - {}".format(item[0], item[1]))
    logger.info(efruits)
    assert [(0, 'apple'),(1, 'pear'),(2,'apricot'),(3,'cherry'),(4,'peach')] == list(enumerate(fruits))

def test_135_unpack(): # 13.5
    ''' Example of unpacking or variadic parameter
    '''
    z = (5,4)
    result=add(*z)
    logger.info(result) # without the *, function expects 2 arguments
    assert 9 == result

def test_1333_pythonic_enumerate_sequence():
    fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
    for n in range(len(fruits)):
        logger.info("{} {}".format(n, fruits[n]))

def test_1333b_pythonic_enumerate_sequence():
    fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
    for item in enumerate(fruits):
        logger.info("{} {}".format(item[0], item[1]))

def test_1341_circleinfo(): # 13.4
  area1, circum1 = circleInfo(10) # auto packing
  (area2, circum2) = circleInfo(100)
  logger.info("area1:{} circum1:{}".format(area1,circum1))
  logger.info("area2:{} circum2:{}".format(area2,circum2))
  assert math.isclose(area1*10,area2)
  assert math.isclose(circum1*100,circum2)

# endregion tests
