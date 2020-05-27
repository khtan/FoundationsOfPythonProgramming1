# region imports
import os
import sys
import logging
import pytest
import io
import json
import copy

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
# region tests for xx.x
def test_172_nested_dictionaries():
    # A dictionary can have both integer and string keys
    dict = {'key1': {'a':5, 'c': 90, 5:50, '5':55}, 'key2':{'b':3, 'c':"yes"}}
    assert 55 == dict['key1']['5']
    assert 50 == dict['key1'][5]

def test_1731_json_loads():
    ''' 17.3 json module : json.loads and json.dumps
        In python/tests, outputs for both python and cs code are in
        test_1731_json_loads.py.org and test_1731_json_loads.cs.org
        Due to logger differences, have to manually view the similarities
    '''
    # 1. Start with a json encoded string, including \n
    a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
    logger.info("1 a_string:\n{}\n:a_string".format(a_string))
    # 2. Use json.loads
    d = json.loads(a_string)
    typed = str(type(d))
    logger.info("2 type: {}".format(typed))
    assert "<class 'dict'>" == typed
    # 3. access dictionary keys
    logger.info("3 d: {}".format(d.keys()))
    # 4. each line in dictionary
    for k in d:
      logger.info("4 {}".format(k))
    # 5. access inner results dictionry
    for i in range(len(d['results'])):
      logger.info("5 {} -> {}".format(i, d['results'][i]))
    # 6. access dictionary element
    logger.info("6 resultCount = {}".format(d['resultCount']))
    assert 25 == d['resultCount']

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
def test_1732_json_dumps():
    ''' This is an example of using json as a utility
      d is a real python dictionary
      To print its structure nicely, the code uses json.dump
    '''
    d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

    logger.info(d)
    # logger.info(pretty(d))
    expected = '''{
  "key1": {
    "5": 50,
    "a": 90,
    "c": true
  },
  "key2": {
    "b": 3,
    "c": "yes"
  }
}'''
    assert expected == pretty(d)
def test_176_deepcopy():
    ''' This test is used to show that Python has a deepcopy utility to deal with nested containers.
        This strategy is different in C# bec C# requires each class to handle its own copy semantics.
        For example, ArrayList has a clone while Dictionary<T> has a copy constructor
    '''
    eoriginal = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]] # expected, unmodified
    original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]    
    shallow_copy_version = original[:]
    deeply_copied_version = copy.deepcopy(original)
    original.append("Hi there")
    original[0].append(["marsupials"])
    eoriginal2 = [['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']], 'Hi there']
    assert eoriginal2 == original
    assert eoriginal == deeply_copied_version
    eoriginal3 = [['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']]]
    assert eoriginal3 == shallow_copy_version
# endregion tests
