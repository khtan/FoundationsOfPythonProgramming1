# region imports
import os
import sys
import logging
import pytest
import io
import math
# from point import Point # this avoids having to use point.Point everywhere else
# from tests.point import Point # VS Code can find file but test discovery does not
from pretty import pretty # first try using this module, C# -- SmartFormat

''' Notes
1. If place point.py in FoundationsOfPythonProgramming/python, VS Code cannot find the file.
2. If place point.py in FoundationsOfPythonProgramming/python/tests, VS Code cannot find the file "from point import Point" but test discovery does
   If test_ch20_class.py uses from tests.point import Point, VS Code finds the file but test discovery does not
3. Temporary solution : put class Point in this file
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
class Point:
    """Point class for representing and manipulating x,y coordinates"""
    def __init__(self, initX=0, initY=0):
        """ create new point at origin """
        self.x = initX
        self.y = initY

    def __str__(self):
        return "<{},{}>".format(self.x, self.y)

    def __pretty__(self, p, cycle):
        p.pretty("<{},{}>".format(self.x, self.y))

    def getX(self): return self.x
    def getY(self): return self.y
    def distanceFromOrigin(self):
        return ((self.getX()**2) + (self.getY()**2)) ** 0.5
    def halfway(self, target):
        mx = (self.getX() + target.getX())/2
        my = (self.getY() + target.getY())/2
        return Point(mx, my)

def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()
    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

# endregion globals
# region helpers
# endregion helpers
# region tests for xx.x
def test_2031_instantiate():
    p = Point() # check instantiation
    logger.info(p)
    assert "<0,0>" == str(p)

    q = Point()
    assert q is not p # confirm two instances are different

def test_2051_distancefromorigin():
    p = Point(7,6)
    d = p.distanceFromOrigin()
    logger.info(d)
    assert math.isclose(9.21954445729, d)

def test_2052_distancefromorigin():
    p = Point(0,0)
    d = p.distanceFromOrigin()
    logger.info(d)
    assert math.isclose(0, d)

def test_2061_class_function():
    p = Point(7,6)
    q = Point(0,0)
    d1 = p.distanceFromOrigin()
    d2 = distance(p,q)
    logger.info(d1)
    assert math.isclose(d1, d2)

def test_2081_midpoint(): # instances as return values
    p = Point(3,4)
    q = Point(5,12)
    midp = p.halfway(q)
    midq = q.halfway(p)
    logger.info(midp)
    # no function yet to allow directly comparing contents of Points
    assert math.isclose(4.0, midp.getX())
    assert math.isclose(8.0, midq.getY())
    assert midp.getX() == midq.getX()
    assert midp.getY() == midq.getY()

def test_2091_sort_pattern():
    '''This is a pattern for sorting lists of objects, without the classical builtin functions
    The text says a bunch of methods or one complicated method
    Uses the key function in sorted
    '''
    lst = [Point(1,5), Point(2,4), Point(3,3), Point(4,2), Point(5,1)]
    sortByX = sorted(lst, key=lambda p: p.getX())
    sortByY = sorted(lst, key=lambda p: p.getY())
    logger.info(pretty(sortByX))
    logger.info(pretty(sortByY))
    # assert the 2 ends are the same
    assert sortByX[0] == sortByY[-1]
    assert sortByX[-1] == sortByY[0]
# endregion tests
