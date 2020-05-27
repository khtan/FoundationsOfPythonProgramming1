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
# region tests for Ch23
def test_2321_map():
    lst = [2,5,9]
    lst3 = list(map(lambda x: 3 * x, lst))
    elst3 = [6, 15, 27]
    assert elst3 == lst3

def test_2321_lc():
    lst = [2,5,9]
    lst3 = [3*x for x in lst]
    elst3 = [6, 15, 27]
    assert elst3 == lst3

def test_2322_map():
    '''  Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
    '''
    lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
    greeting_doubled = list(map(lambda x : 2 * x , lst))
    logger.info(greeting_doubled)
    elst = [["hi", "bye", "hi", "bye"], "hellohello", "goodbyegoodbye", [9, 2, 9, 2], 8]
    assert elst == greeting_doubled
def test_2322_lc(): # list comprehension version
    lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
    greeting_doubled = [ 2 * x for x in lst]
    logger.info(greeting_doubled)
    elst = [["hi", "bye", "hi", "bye"], "hellohello", "goodbyegoodbye", [9, 2, 9, 2], 8]
    assert elst == greeting_doubled

def test_2323_map():
    ''' Below, we have provided a list of strings called abbrevs. 
    Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.
    '''
    abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
    abbrevs_upper = list(map(lambda s: s.upper(),abbrevs))
    # logger.info(abbrevs_upper)
    eabbrevs = ["USA", "ESP", "CHN", "JPN", "MEX", "CAN", "RUS", "RSA", "JAM"]
    assert eabbrevs == abbrevs_upper

def test_2323_lc(): 
    abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
    abbrevs_upper = [ s.upper() for s in abbrevs]
    # logger.info(abbrevs_upper)
    eabbrevs = ["USA", "ESP", "CHN", "JPN", "MEX", "CAN", "RUS", "RSA", "JAM"]
    assert eabbrevs == abbrevs_upper

def test_2331_filter():
    lst = [3, 4, 6, 7, 0, 1]
    evens = list(filter(lambda x : x % 2 == 0,lst))
    elst = [4, 6, 0]
    assert elst == evens

def test_2331_lc():
    lst = [3, 4, 6, 7, 0, 1]
    evens = [x for x in lst if x % 2 == 0]
    elst = [4, 6, 0]
    assert elst == evens

def test_2332_filter():
    ''' Write code to assign to the variable filter_testing all the elements in lst_check
    that have a w in them using filter.
    '''
    lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
    filter_testing = list(filter(lambda w : "w" in w,lst_check))
    elst = ['watermelon', 'kiwi', 'strawberries']
    assert elst == filter_testing

def test_2332_lc():
    lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
    filter_testing = [w for w in lst_check if "w" in w]
    elst = ['watermelon', 'kiwi', 'strawberries']
    assert elst == filter_testing

def test_2341_mapfilter():
    things = [3, 4, 6, 7, 0, 1]
    #chaining together filter and map:
    # first, filter to keep only the even numbers
    # double each of them
    lst = list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))
    elst = [8, 12, 0]
    assert elst == lst

def test_2341_lc():
    things = [3, 4, 6, 7, 0, 1]
    lst = [x*2 for x in things if x % 2 == 0]
    elst = [8, 12, 0]
    assert elst == lst

def test_2342_dict_mapfilter():
    tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
    compri = list(
        map( lambda item: item['name'], 
           filter(lambda item: 'name' in item , tester['info'])
        )
    )
    ecompri = ['Lauren', 'Ayo', 'Kathryn', 'Nick', 'Gladys', 'Adam']
    assert ecompri == compri

def test_2342_dict_lc():
    ''' Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. 
    Do this using a list comprehension.
    '''
    tester = {'info': [
        {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
        {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, 
        {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, 
        {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, 
        {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, 
        {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
    compri = [item['name'] for item in tester['info'] if 'name' in item]
    logger.info(compri)
    ecompri = ['Lauren', 'Ayo', 'Kathryn', 'Nick', 'Gladys', 'Adam']
    assert ecompri == compri

def test_2351_zip():
    L1 = [3, 4, 5]
    L2 = [1, 2, 3]
    L3 = []
    L4 = list(zip(L1, L2))
    for (x1, x2) in L4:
        L3.append(x1+x2)
    logger.info(L3)
    eL3 = [4, 6, 8]
    assert eL3 == L3
def test_2351_zip_map():
    L1 = [3, 4, 5]
    L2 = [1, 2, 3]
    L3 = []
    L3 = list(map(lambda tp : tp[0] + tp[1], (zip(L1, L2))))
    logger.info(L3)
    eL3 = [4, 6, 8]
    assert eL3 == L3

def test_2351_zip_lc():
    L1 = [3, 4, 5]
    L2 = [1, 2, 3]
    L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
    eL3 = [4, 6, 8]
    assert eL3 == L3

@pytest.mark.skip(reason="Python zip does not have resultSelector")
def test_extra_zip_resultselector():
    pass


# endregion tests
