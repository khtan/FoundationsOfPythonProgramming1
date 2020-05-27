# region imports
import sys
import logging
import pytest
import io
from unittest.mock import patch

# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers

# endregion helpers
# region 9.7 mutating methods
def test_971_listmethods():
    mylist = []
    mylist.append(5)
    mylist.append(27)
    mylist.append(3)
    mylist.append(12)
    logger.info(mylist)
    logger.info("--- mutable, insert an item 12 at pos 1")
    mylist.insert(1, 12)
    logger.info(mylist)
    logger.info("count of 12: %s", mylist.count(12))
    logger.info("--- immutable, get info on list")
    logger.info("   index of 3: %s", mylist.index(3))
    logger.info("   count of 5 : %s", mylist.count(5))
    logger.info("--- mutable, reverse")
    mylist.reverse()
    logger.info(mylist)
    logger.info("--- mutable, sort")
    mylist.sort()
    logger.info(mylist)
    logger.info("--- mutable, item 5")
    mylist.remove(5)
    logger.info(mylist)
    logger.info("--- mutable, pop with no argument")
    lastitem = mylist.pop()
    logger.info("lastitem: %s", lastitem)
    logger.info("mylist: %s", mylist)
def test_972_sort_returns_none():
    mylist = []
    mylist.append(5)
    mylist.append(27)
    mylist.append(3)
    mylist.append(12)
    logger.info("list: %s", mylist)

    mylist = mylist.sort()   #probably an error bec list is mutated, return value is always None
    logger.info("after assignment, list: %s", mylist)
# endregion  9.7 mutating methodstests
# region 9.8 append vs concat
def test_981_append():
    origlist = [45,32,88]
    origlist.append("cat")
    logger.info("after append: %s", origlist)
def test_982_concat():
    origlist = [45,32,88]
    id1 = id(origlist)
    logger.info("id1 : %s", id1)
    origlist = origlist + ["cat"] # need to put cat in list
    logger.info("after concat %s", origlist)
    id2 = id(origlist)
    logger.info("id2 : %s", id2)
    assert id1 != id2 # concat returns new reference
def test_983_plusequal_appends():
    '''
       The code below, when copied from browser contained tabs, causing python to fail to compile
       The error in aliaslist = origlist was "Unable to assign to error expression", totally missing the tab/space problem.

       By convention, indentation should be spaces.
       Python3 does not allow mixing spaces and tabs.
    '''
    origlist = [45,32,88]
    aliaslist = origlist
    logger.info("origlist: %s", origlist)
    logger.info("id of origlist: %s, id of aliaslist: %s", id(origlist), id(aliaslist))
    origlist += ["cat"] # appends to original list
    logger.info("origlist after +=: %s", origlist)
    logger.info("id of origlist: %s, id of aliaslist: %s", id(origlist), id(aliaslist))
    origlist = origlist + ["cow"] # concat, creates new reference
    logger.info("origlist after +: %s", origlist)
    logger.info("id of origlist: %s, id of aliaslist: %s", id(origlist), id(aliaslist))
'''
Make a new list from a string where each element of the list is a character in the string
Perl will split on empty string but Python does not
   ValueError: empty separator
'''
def test_984_list_from_string():
    st = "Warmth"
    a = []
    id1 = id(a)
    logger.info("id1 of a: %s", id1)
    for char in st:
        a.append(char)
        logger.info("loop - id of a: %s", id(a))
    id2 = id(a)
    logger.info("id2 of a: %s", id2)
    logger.info(a)
    assert id1 == id2
def test_985_list_from_string():
    st = "Warmth"
    a = []
    id1 = id(a)
    logger.info("id1 of a: %s", id1)
    for char in st:
        a += [char]
        logger.info("loop - id of a: %s", id(a))
    id2 = id(a)
    logger.info("id2 of a: %s", id2)
    logger.info(a)
    assert id1 == id2
# for loop is smart enough to copy the final array beck to original 'a' at the end of loop
def test_986_list_from_string():
    st = "Warmth"
    a = []
    id1 = id(a)
    logger.info("id1 of a: %s", id1)
    for char in st:
        a = a + [char]
        logger.info("loop - id of a: %s", id(a))
    id2 = id(a)
    logger.info("id2 of a: %s", id2)
    logger.info(a)
    assert id1 == id2
# endregion 9.8 append vs concat
# region 9.9 non-mutating methods on strings
def test_991_upper_and_lower():
    ss = "Hello, World"
    logger.info(ss.upper())

    tt = ss.lower()
    logger.info("tt=%s",tt)
    logger.info("ss=%s", ss)
def test_992_count_strip_replace():
    ss = "    Hello, World    " # tabs inserted in front and back

    els = ss.count("l")
    logger.info("els = %s", els)

    logger.info("stripping : %s", "***"+ss.strip()+"***")

    news = ss.replace("o", "***")
    logger.info("news = %s", news)
def test_993_format(): # This uses unittest.patch
    name='Einstein'
    with patch('builtins.input', return_value=name), patch('sys.stdout', io.StringIO()) as mock_output:
       person = input('Enter your name: ')
       print('Hello {}!'.format(person))
       assert mock_output.getvalue().strip() == "Hello {}!".format(name)
def test_993a_format(mocker): # This uses pytest-mock mocker
    name='Einstein'
    mocker.patch('builtins.input', return_value=name)
    mock_output = mocker.patch('sys.stdout', io.StringIO())
    person = input('Enter your name: ')
    print('Hello {}!'.format(person))
    assert mock_output.getvalue().strip() == "Hello {}!".format(name)
def test_994_format():
    scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
    for person in scores:
        name = person[0]
        score = person[1]
        logger.info("Hello {}. Your score is {}.".format(name, score))
def test_985_format():
    origPrice = 17.0
    discount = 20
    # origPrice = float(input('Enter the original price: $'))
    # discount = float(input('Enter discount percentage: '))
    newPrice = (1 - discount/100)*origPrice
    result = '${} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
    logger.info(result)
    expected = "$17.0 discounted by 20% is $13.60."
    assert result == expected
def test_986_insufficient_parameters_format():
    name = "Sally"
    greeting = "Nice to meet you"
    s = "Hello, {}. {}."

    s1 = s.format(name,greeting) # will print Hello, Sally. Nice to meet you.
    s2 = s.format(greeting,name) # will print Hello, Nice to meet you. Sally.
    with pytest.raises(IndexError):
        s3 = s.format(name) # 2 {}s, only one interpolation item! Not ideal.
    assert s1 == "Hello, Sally. Nice to meet you."
    assert s2 == "Hello, Nice to meet you. Sally."
def test_987_doublebraces():
# Info about \{\{ in text is incorrect
    a = 5
    b = 9
    s1 = "{{a}} = {0}".format(a)
    s2 = "{{a}} = {}".format(a)
    s3 = "{{{},{}}}".format(a,b)
    assert s1 == "{a} = 5"
    assert s2 == "{a} = 5"
    assert s3 == "{5,9}"
def test_988_float():
    v = 2.34567
    s = '{:.1f} {:.2f} {:.7f}'.format(v,v,v)
    assert s == "2.3 2.35 2.3456700"
def test_9100_ing():
    # For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
    verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
    ing1 = []
    ing2 = []
    ing3 = []
    for verb in verbs:
        ing1.append(verb + "ing")      # append
        ing2 = ing2 + [ verb + "ing"]  # insert
        ing3 += [ verb + "ing" ]       # clone
    assert ing1 == ing2
    assert ing2 == ing3
def test_9101_list_accumulator():
    # Given the list of numbers, numbs, create a new list of those same numbers increased by 5. 
    # Save this new list to the variable newlist.
    numbs = [5, 10, 15, 20, 25]
    newlist = []
    for num in numbs:
        newlist = newlist + [num +5]
    logger.info(newlist)
def test_9101_list_accumulatorA():
    # Now do the same as in the previous problem, but do not create a new list. 
    # Overwrite the list numbs so that each of the original numbers are increased by 5
    numbs = [5, 10, 15, 20, 25]
    for idx in range(len(numbs)):
        numbs[idx] = numbs[idx] + 5
    logger.info(numbs)
def test_9102_string_accumulator():
    s = "ball"
    r = ""
    for item in s:
        r = item.upper() + r
    logger.info(r)
    assert r == "LLAB"
def test_string_format_operator():

    name = "Anaconda"
    s1 = "Hello {}". format(name) # new
    s2 = "Hello %s" % name        # old
    logger.info(s1)
    logger.info(s2)
    assert s1 == s2
# endregion 9.9 non-mutating methods on strings
# region 9.15 exercises
def test_915_1():
    ''' For each word in the list verbs, add an -ing ending. 
       Overwrite the old list so that verbs has the same words with ing at the end of each one.
    '''
    verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
    logger.info("Before: {}".format(verbs))
    for idx in range(len(verbs)):
        verbs[idx] = verbs[idx] + "ing"
    logger.info("After: {}".format(verbs))
    expected = ["kayaking", "crying", "walking", "eating", "drinking", "flying"]    
    assert verbs == expected
def test_915_2():
    ''' In XYZ University, upper level math classes are numbered 300 and up.
        Upper level English classes are numbered 200 and up.
        Upper level Psychology classes are 400 and up.
        Create two lists, upper and lower.
        Assign each course in classes to the correct list, upper or lower.
        HINT: remember, you can convert some strings to different types!
    '''
    classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
    upper = []
    lower = []
    for classname in classes:
        (subject, level) = classname.split()
        nlevel = int(level)
        isClassUpper = False
        if(subject == "MATH"):
            if(nlevel >= 300): isClassUpper = True
        elif(subject == "ENG"):
            if(nlevel >= 200): isClassUpper = True
        elif(subject == "PSYCH"):
            if(nlevel >= 400): isClassUpper = True
        else:
            logger.info("Warning: subject is not valid")
        if(isClassUpper):
            upper += [classname]
        else:
            lower += [classname]
    logger.info("upper : {}".format(upper))
    logger.info("lower : {}".format(lower))
    assert len(upper) == 6
    assert len(classes) == len(upper) + len(lower)
def test_915_3():
    ''' Starting with the list myList = [76, 92.3, ‘hello’, True, 4, 76], 
        write Python statements to do the following:
           Append “apple” and 76 to the list.
           Insert the value “cat” at position 3.
           Insert the value 99 at the start of the list.
           Find the index of “hello”.
           Count the number of 76s in the list.
           Remove the first occurrence of 76 from the list.
           Remove True from the list using pop and index.
        kht: Might be interesting to reimplment all these in terms of slicing operator
    '''
    myList = [76, 92.3, 'hello', True, 4, 76]
    myList.append("apple")
    myList.append(76)
    logger.info("After append: {}".format(myList))
    myList.insert(3, "cat")
    logger.info("After insert 'cat' at pos 3: {}".format(myList))
    myList.insert(0, 99)
    logger.info("After insert 99 at start: {}".format(myList))
    helloIndex = myList.index("hello")
    logger.info("helloIndex: {}".format(helloIndex))
    countOf76 = myList.count(76)
    logger.info("countOf76: {}".format(countOf76))
    myList.remove(76)
    logger.info("After removing first occurence of 76: {}".format(myList))
    indexOfTrue = myList.index(True)
    myList.pop(indexOfTrue)
    logger.info("After popping True: {}".format(myList))    
def test_915_4():
    ''' The module keyword determines if a string is a keyword.
    e.g. keyword.iskeyword(s) where s is a string will return either True or False,
    depending on whether or not the string is a Python keyword.
    Import the keyword module and test to see whether each of the words in list test are keywords.
    Save the respective answers in a list, keyword_test.
    Strange that str, string and String are not keywords
    '''
    import keyword
    test = ["else", "integer", "except", "elif", "str", "string", "String"]
    keywords = []
    keyword_test = []
    for word in test:
        answer = keyword.iskeyword(word)
        keyword_test.append(answer)
        if answer:
            keywords.append(word)
    logger.info("keyword_test : {}".format(keyword_test))
    logger.info("keywords : {}".format(keywords))
def test_915_5():
    '''The string module provides sequences of various types of Python characters. 
    It has an attribute called digits that produces the string ‘0123456789’. 
    Import the module and assign this string to the variable nums. 
    Below, we have provided a list of characters called chars. 
    Using nums and chars, produce a list called is_num that consists of tuples. 
    The first element of each tuple should be the character from chars, 
    and the second element should be a Boolean that reflects whether or not it is a Python digit.
    '''
    import string
    chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']
    nums = string.digits
    is_num = []
    for char in chars:
        is_num.append((char, char in nums))
    logger.info("is_num: {}".format(is_num))
# endregion 9.15 exercises
# region slice
''' The slice operator is a very versatile one that can be used to pop, insert, append, etc.
This region proposed to show how to do this both for list and string
   slice(start [optional, defaults to None], stop, step [optional, defaults to None])
      start = starting index
      stop = slicing stops at stop-1(last element)
      step = incremetn for slicing
   append
https://www.journaldev.com/23584/python-slice-string
https://www.programiz.com/python-programming/methods/built-in/slice
Q) How is operator [::] mapped to slice(start, stop, step)?
'''
def exercise_slice_immutable(s, first, last, reverse): # iterable and expected results
    # identity
    assert s == s[:]
    assert s == s[::]
    for i in range(len(s)+2): # includes overindexing
        assert s == s[:i] + s[i:]
    # first element
    assert s[0] == first
    # last element
    assert s[-1] == last
    # reverse
    r = s[::-1]
    assert r == reverse
def exercise_sublist_immutable(s, leftover_unit, delete_unit):
    # sublist
    assert s[1:3] == delete_unit
    # delete
    t = s[0:1] + s[3:]
    assert t == leftover_unit
    # insert
    u = t[0:1] + delete_unit + t[1:]
    assert u == s

def test_slice_list():
    s = ["a", "b", "c", "d", "e"]
    r = ["e", "d", "c", "b", "a"]
    exercise_slice_immutable(s, "a", "e", r)
    exercise_sublist_immutable(s, ["a", "d", "e"], ["b", "c"])
    # delete
    s[1:3] = []
    assert s == ["a", "d", "e"]
    # insert
    s[1:1] = ["b", "c"]
    assert s == ["a","b","c","d","e"]
def test_slice_tuple():
    s = ("a", "b", "c", "d", "e")
    r = ("e","d","c","b","a")
    exercise_slice_immutable(s, "a", "e", r)
    exercise_sublist_immutable(s, ("a","d", "e"), ("b","c"))
def test_slice_string():
    s = "hello"
    r = "olleh"
    exercise_slice_immutable(s, "h", "o", r)
    exercise_sublist_immutable(s, "hlo", "el")
# endregion slice
# region 9.16 assessment
def test_916_alias():
    x = ["dogs", "cats", "birds", "reptiles"]
    y = x
    x += ['fish', 'horses']
    y = y + ['sheep']
    logger.info("x is {}".format(x))
    logger.info("y is {}".format(y))
    assert x.count('sheep') == 0 # x does not see 'sheep' bec y is already cloned
def test_917_word_lengths():
    original_str = "The quick brown rhino jumped over the extremely lazy fox"
    num_words_list = []
    for word in original_str.split():
        num_words_list.append(len(word))
    logger.info(num_words_list)
    assert num_words_list == [3, 5, 5, 5, 6, 4, 3, 9, 4, 3]
def test_918_acronynm():
    '''
        Write code that uses the string stored in org and creates an acronym 
        which is assigned to the variable acro. 
        Only the first letter of each word should be used, 
        each letter in the acronym should be a capital letter, 
        and there should be nothing to separate the letters of the acronym. 
        Words that should not be included in the acronym are stored in the list stopwords. 
        For example, if org was assigned the string “hello to world” 
        then the resulting acronym should be “HW”.    
    '''
    stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
    org = "The organization for health, safety, and education"
    acro = ""
    for word in org.split():
        if word not in stopwords:
            acro = acro + word[0].upper()
    logger.info(acro)
    assert acro == "OHSE"
def test_919_palindrome():
    '''
       A palindrome is a phrase that, if reversed, would read the exact same.
       Write code that checks if p_phrase is a palindrome by reversing it and then
       checking if the reversed version is equal to the original.
       Assign the reversed version of p_phrase to the variable r_phrase
       so that we can check your work.
    '''
    p_phrase = "was it a car or a cat I saw"
    r_phrase = p_phrase[::-1] # slice
    r_phrase2 = " ".join(reversed(p_phrase)) # join-reversed
    logger.info(p_phrase == r_phrase)
    logger.info(p_phrase == r_phrase2)
def test_920_inventory():
    '''
       Provided is a list of data about a store’s inventory where each item in the list
       represents the name of an item, how much is in stock, and how much it costs.
       Print out each item in the list with the same formatting, using the .format method
       (not string concatenation).
       For example, the first print statment should read
       The store has 12 shoes, each for 29.99 USD.
    '''
    inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
    for item in inventory:
        (name, qty, unitcost) = item.split(',')
        logger.info("The store has {} {}, each for {} USD.".format(qty.strip(), name, unitcost.strip()))
def test_920a_inventory():
    '''
       Provided is a list of data about a store’s inventory where each item in the list
       represents the name of an item, how much is in stock, and how much it costs.
       Print out each item in the list with the same formatting, using the .format method
       (not string concatenation).
       For example, the first print statment should read
       The store has 12 shoes, each for 29.99 USD.
    '''
    inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
    for item in inventory:
        (name, qty, unitcost) = item.split(", ")
        logger.info("The store has {} {}, each for {} USD.".format(qty, name, unitcost))
# endregion 9.16 assessment