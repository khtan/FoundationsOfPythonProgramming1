#imports
import sys
import logging
import pytest

# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers

# endregion helpers
# region tests
'''
rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma.
Write code to compute the number of months that have more than 3 inches of rainfall.
Store the result in the variable num_rainy_months.
In other words, count the number of items with values > 3.0.
'''
def test_1():
    rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
    rainfall_string_array = rainfall_mi.split(",")
    num_rainy_months = 0
    for rain_string in rainfall_string_array:
        if float(rain_string) > 3:
            num_rainy_months += 1
    logger.info(num_rainy_months)
    assert num_rainy_months == 5
'''
The variable sentence stores a string. Write code to determine how many words in sentence
start and end with the same letter, including one-letter words.
Store the result in the variable same_letter_count.
'''
def test_2():
    sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
    same_letter_count = 0
    words = sentence.split(" ")
    for word in words:
        if word[0] == word[-1]:
            same_letter_count += 1
    logger.info(same_letter_count)
    assert same_letter_count == 2
'''
Write code to count the number of strings in list items that have the character w in it.
Assign that number to the variable acc_num.

HINT 1: Use the accumulation pattern!
HINT 2: the in operator checks whether a substring is present in a string.
'''
def test_3():
    items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
    acc_num = 0
    for item in items:
        if item.count("w") > 0:
            acc_num += 1
    logger.info(acc_num)
    assert acc_num == 4
def test_3a():
    items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
    acc_num = 0
    for item in items:
        if "w" in item:
            acc_num += 1
    logger.info(acc_num)
    assert acc_num == 4
'''
Write code that counts the number of words in sentence that contain either an “a” or an “e”.
Store the result in the variable num_a_or_e.

Note 1: be sure to not double-count words that contain both an a and an e.
HINT 1: Use the in operator.
HINT 2: You can either use or or elif.
'''
def test_4():
    sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
    num_a_or_e = 0
    words = sentence.split(" ")
    for word in words:
        if "a" in word or "e" in word :
            num_a_or_e += 1
    logger.info(num_a_or_e)
    assert num_a_or_e == 14
'''
Write code that will count the number of vowels in the sentence s and
assign the result to the variable num_vowels.
For this problem, vowels are only a, e, i, o, and u.
Hint: use the in operator with vowels.
'''
def test_5():
    s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
    vowels = ['a','e','i','o','u']
    num_vowels = 0
    sa = s.split(" ")
    for word in sa:
        num_vowels += word.count("a")
        num_vowels += word.count("e")
        num_vowels += word.count("i")
        num_vowels += word.count("o")
        num_vowels += word.count("u")
    logger.info(num_vowels)
    assert num_vowels == 32

def test_5a():
    s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
    vowels = ['a','e','i','o','u']
    num_vowels = 0
    for char in s:
       if char in vowels:
           num_vowels += 1
    logger.info(num_vowels)
    assert num_vowels == 32
'''
Create one conditional so that if “Friendly” is in w, then “Friendly is here!”
should be assigned to the variable wrd.
If it’s not, check if “Friend” is in w.
If so, the string “Friend is here!” should be assigned to the variable wrd,
otherwise “No variation of friend is in here.” should be assigned to the variable wrd.
(Also consider: does the order of your conditional statements matter for this problem? Why?)
'''
def test_6():
    w = "Friendship is a wonderful human experience!"
    if "Friendly" in w:
        wrd = "Friendly is here!"
    elif "Friend" in w:
        wrd = "Friend is here!"
    else:
       wrd = "No variation of friend is in here"
    logger.info(wrd)
    assert wrd == "Friend is here!"
'''
We have written conditionals for you to use.
Create the variable x and assign it some integer so that at the end of the code,
output will be assigned the string "Consistently working".
'''
def test_7():
    x = 8
    if x >= 10:
        output = "working"
    else:
        output = "Still working"
    if x > 12:
        output = "Always working"
    elif x < 7:
        output = "Forever working"
    else:
        output = "Consistently working"
    assert output == "Consistently working"
'''
Write code so that if "STATS 250" is in the list schedule,
then the string "You could be in Information Science!" is assigned to the variable resp.
Otherwise, the string "That's too bad." should be assigned to the variable resp.
'''
def test_8():
   schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]

   resp = "That's too bad."
   for subject in schedule:
      if subject == "STATS 250":
          resp = "You could be in Information Science!"
   print(resp)
   assert resp == "You could be in Information Science!"
   logger.info(resp)
'''
Create the variable z whose value is 30.
Write code to see if z is greater than y.
If so, add 5 to y’s value, otherwise do nothing.
Then, multiply z and y, and assign the resulting value to the variable x.
'''
def test_9():
    y = 22
    z = 30
    if z > y:
        y = y + 5
    x = z * y
    logger.info(x)
    assert x == 810
    assert z == 30
'''
For each string in wrd_lst, find the number of characters in the string.
If the number of characters is less than 6, add 1 to accum so that in the end,
accum will contain an integer representing the total number of words in the list
that have fewer than 6 characters.
'''
def test_10():
    wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
    accum = 0
    for word in wrd_lst:
        if len(word) < 6:
            accum += 1
    logger.info(accum)
    assert accum == 5
# endregion tests
