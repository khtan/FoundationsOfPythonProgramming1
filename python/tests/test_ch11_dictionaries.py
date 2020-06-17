# region imports
import os
import sys
import logging
import pytest
import io
import math
import re
from unittest.mock import patch
''' Notes
Creation: map = {} # empty map
          map = {k1:v1,k2:v2} # key value creation
Operators:
          map[k]=v # create entry by insertion
          del map[y] # delete item VS map[y] = <zero>
Methods:
          map.keys() # list of keys, in unknown order
          map.items() # list of tuple items, in unknown order
          map.values() # list of values, in unknown order
          map.get(key) # returns value else None
          map.get(key, alt-value) # returns value, else alt-value
          for key in map.keys() === for key in map
          len(map)
          map.copy()
Issues:
1) The data file 'scarlet.txt' could not be accessed - button does not work
   Downloaded copy is slightly different from coursera's - so counts are different.

'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers
# endregion helpers
# region tests for 11
def test_116_1():
    ''' 11.6 Intro: accumulating multiple results in a dictionary
    3. Create a dictionary called char_d from the string stri, so that the key is a character
       and the value is how many times it occurs.
    '''
    stri = "what can I do"
    char_d = {}
    for char in stri:
       if char not in char_d:
          char_d[char] = 0
       char_d[char] += 1
    logger.info(char_d)
    expected = {'w': 1, 'h': 1, 'a': 2, 't': 1, ' ': 3, 'c': 1, 'n': 1, 'I': 1, 'd': 1, 'o': 1}
    assert expected == char_d
def test_116_2():
    # f = open('../data/scarlet.txt', 'r')  # python 3.8.0 fails because of encoding
    # documentation that says python3 open uses utf-8 by default is incorrect
    f = open('../data/scarlet.txt', 'r', encoding='utf-8')

    txt = f.read()
    # now txt is one long string containing all the characters
    letter_counts = {} # start with an empty dictionary
    for c in txt:
        if c not in letter_counts:
            # we have not seen this character before, so initialize a counter for it
            letter_counts[c] = 0
        #whether we've seen it before or not, increment its counter
        letter_counts[c] = letter_counts[c] + 1
    # logger.info(letter_counts)
    expected={'\ufeff': 1, 'T': 700, 'h': 12893, 'e': 25415, ' ': 43585, 'P': 203, 'r': 12055, 'o': 15507, 'j': 214, 'c': 5123, 't': 17587, 'G': 235, 'u': 5663, 'n': 13716, 'b': 2741, 'g': 4018, 'E': 270, 'B': 156, 'k': 1480, 'f': 4223, 'A': 389, 'S': 405, 'd': 9014, 'y': 3720, 'I': 1358, 'a': 15873, 'l': 7445, ',': 3137, 'C': 186, 'D': 205, '\n': 5156, 'i': 12696, 's': 11831, 'w': 4745, 'm': 5098, 'v': 1906, '.': 2786, 'Y': 201, 'p': 3338, '-': 610, 'L': 256, ':': 92, 'J': 116, '1': 102, '2': 54, '0': 30, '8': 23, '[': 51, '#': 1, '4': 32, ']': 51, 'R': 181, '9': 21, '5': 21, 'U': 84, '3': 31, '6': 20, 'F': 206, '*': 28, 'O': 193, 'H': 546, 'N': 240, 'K': 20, 'q': 153, '’': 502, 'x': 330, '7': 16, '\t': 1, 'M': 191, '(': 23, '_': 34, 'W': 286, ')': 23, 'z': 140, '“': 937, '”': 857, '?': 208, '!': 86, ';': 104, 'V': 30, '‘': 90, 'Q': 2, 'è': 1, 'é': 2, 'ñ': 4, 'Z': 2, '&': 2, '"': 1, '/': 25, '%': 1, 'X': 2, '@': 2, '$': 2}
    assert expected == letter_counts
def test_117_scrabble_score():
    f = open('../data/scarlet.txt', 'r', encoding="utf-8")
    txt = f.read()
    # now txt is one long string containing all the characters
    char_counts = {} # start with an empty dictionary
    for c in txt:
        if c not in char_counts:
            # we have not seen this character before, so initialize a counter for it
            char_counts[c] = 0

        #whether we've seen it before or not, increment its counter
        char_counts[c] = char_counts[c] + 1

    letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

    score = 0
    for y in char_counts:
        if y in letter_values:
            score = score + letter_values[y] * char_counts[y]
    logger.info(score)
    # python code returns 337353 for coursera, but the scarlet.txt could not be accessed
    # the downloaded scarlet.txt currently returns 337382
    assert 337382 == score
def test_118_bestkey():
    ''' 
    Write a program that finds the key in a dictionary that has the maximum value. 
    If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code
    '''
    d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

    ks = d.keys()
    # initialize variable best_key_so_far to be the first key in d
    bestkey = 'a'    
    for k in ks:
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far
       if d[k] > d[bestkey]:
           bestkey = k
           logger.info("key " + bestkey + " has the highest value, " + str(d[bestkey]))
    logger.info(bestkey)
    expected = 312
    assert expected == d[bestkey]
def test_118_bestitem():
    ''' 
    Change algo to keep best item, then can show both key and value
    The map interface does not recognize item in a primary way.
    There should be a function map.getitem(key) to return the tuple
    Makes it more useful.
    '''
    d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

    # initialize variable best_key_so_far to be the first key in d
    bestitem=()
    for k,v in d.items():
        if bestitem == ():
            bestitem = (k,v)
        if d[k] > bestitem[1]:
           bestitem = (k,v)
    logger.info("key " + bestitem[0] + " has the highest value, " + str(bestitem[1]))
    logger.info(bestitem[1])
    expected = 312
    assert expected == bestitem[1]

def test_11112_pirate(): # 11.11 exercises
   '''
   Here’s a table of English to Pirate translations

   | English    | Pirate        |
   |------------+---------------|
   | sir        | matey         |
   | hotel      | fleabag inn   |
   | student    | swabbie       |
   | boy        | matey         |
   | madam      | proud beauty  |
   | professor  | foul blaggart |
   | restaurant | galley        |
   | your       | yer           |
   | excuse     | arr           |
   | students   | swabbies      |
   | are        | be            |
   | lawyer     | foul blaggart |
   | the        | th’           |
   | restroom   | head          |
   | my         | me            |
   | hello      | avast         |
   | is         | be            |
   | man        | matey         |
   |            |               |

   Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.
   '''
   English2Pirate={'sir':'matey','hotel':'fleabag inn','student':'swabbie','boy':'matey','madam':'proud beauty','professor':'foul blaggart','restaurant':'galley','your':'yer','excuse':'arr','students':'swabbies','are':'be','lawyer':'foul blaggart','the':'th’','restroom':'head','my':'me','hello':'avast','is':'be','man':'matey'}
   EnglishSentences=[
    'Hello boy, how are you?',
    'hello boy, how are you?',
    'Good morning sir and madam!',
    'Excuse me, where is the restroom?'
   ]
   CapEnglish2Pirate={} # temporary map to get capitalized words
   for english in English2Pirate:
      capEnglish = english.capitalize()
      CapEnglish2Pirate[english.capitalize()] = English2Pirate[english].capitalize()
   # merge the 2 dictionaries
   English2Pirate.update(CapEnglish2Pirate)    
   
   for line in EnglishSentences:
      pirateLine = []
      for word in line.split():
        filteredWord = re.sub('\W+','',word) # take out any punctuations etc
        if (filteredWord in English2Pirate):
            pirateLine.append(word.replace(filteredWord, English2Pirate[filteredWord]))
        else:
            pirateLine.append(word)
      logger.info("p ={0}".format(pirateLine))

# endregion tests
