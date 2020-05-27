# region imports
import os
import sys
import logging
import pytest
import io
import math
from unittest.mock import patch
''' Notes
1. Modified code to eliminate \r\n and \n so that character counts is consistent between Python, Java and CSharp
   The num_char therefore do not match what "wc" thinks is the number of characters bec that includes the line delimiters
   wc on school_prompt2.txt returns 10 87 547
2. File reading methods - filevar.read(), filevar.readline(), filevar.readlines()
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
''' Simple way to switch between 2 files for test_1031_* 
filepath1 = "../data/twolines.txt"
expected_num_char1 = 17
'''
filepath1 = "../data/school_prompt2.txt"
expected_num_char1 = 527

# endregion globals
# region helpers
# endregion helpers
# region tests for 10.3
def test_1031_num_char_read():
    '''
    Using the file school_prompt2.txt, find the number of characters in the file and 
    assign that value to the variable num_char.
    '''
    with open(filepath1, "r") as f:
        rawString:str = f.read()
        noWhiteSpace = rawString.replace("\r\n", "").replace("\n","")
        num_char = len(noWhiteSpace)
        logger.info("num_char: {}".format(num_char))
        # assert 537 == num_char
        assert expected_num_char1 == num_char    

def test_1031_num_char_readlines():
    with open(filepath1, "r") as f:
        num_char = 0
        for line in f.readlines():
            strippedline = line.strip()
            logger.info(">{}<".format(strippedline))
            num_char += len(strippedline)
        logger.info("num_char: {}".format(num_char))
        assert expected_num_char1 == num_char

def test_1031_num_char_readline():
    with open(filepath1, "r") as f:
        num_char = 0
        line = f.readline().strip()    
        while(line != ""):
            num_char += len(line)
            line = f.readline().strip()
        assert expected_num_char1 == num_char

def test_1031_num_char_fileref(): # file opening idiom
    with open(filepath1, "r") as f:
        num_char = 0
        for line in f:
            num_char += len(line.strip())
        assert expected_num_char1 == num_char

'''
Find the number of lines in the file, travel_plans2.txt, and 
assign it to the variable num_lines.
'''
def test_1032_num_lines_readlines():
    with open("../data/travel_plans2.txt", "r") as f:
        lines = f.readlines()    
        num_lines = len(lines)
        assert 11 == num_lines

def test_1032_num_lines_readline():
    with open("../data/travel_plans2.txt", "r") as f:
        num_lines=0
        line = f.readline()
        while(line != ""):
            num_lines += 1
            line = f.readline()
        assert 11 == num_lines

'''
Create a string called first_forty that is comprised of the first 40 
characters of emotion_words2.txt.
'''
def test_1033_first_forty():
    with open("../data/emotion_words2.txt", "r") as f:
        first_forty = f.read(40)    
        assert "Sad upset blue down melancholy somber bi" == first_forty

def test_1041():
    with open("../data/olympics.txt", "r") as f:
        for line in f.readlines():
            values = line.split(",")
            # logger.info(values[0], "is from", values[3], "and is on the roster for", values[4])
            logger.info("{} is from {} and is on the roster for {}".format(values[0], values[3], values[4]))

def test_1080():
    # 10.8 Writing Text Files
    with open("../data/squared_numbers.txt", "w") as f:
        for number in range(1,13):
            square = number * number
            f.write(str(square) + "\n")
    with open("../data/squared_numbers.txt", "r") as f:
        # logger.info(f.read()[:10]) # print the first 10 characters
        first_ten_chars = f.read(10)
        logger.info(first_ten_chars) # better, read the first 10 characters, then print
    assert "1\n4\n9\n16\n2" == first_ten_chars

def test_1014_1():
   ''' 10.14 Exercises Q1
   The following sample file called studentdata.txt contains one line for each student in an imaginary class.
   The students name is the first thing on each line, followed by some exam scores.
   The number of scores might be different for each student.
   '''
   with open("../data/studentdata.txt", "r") as f:
      for line in f:
         sarray = line.split(" ")
         if len(sarray) > 7:
            logger.info(sarray[0])

def test_1014_2():
   ''' 10.14 Exercises Q2
   Create a list called destination using the data stored in travel_plans.txt.
   Each element of the list should contain a line from the file that lists a country and cities inside that country.
   Hint: each line that has this information also has a colon : in it.
   '''
   destination=[]
   with open("../data/travel_plans2.txt", "r") as f:
       for line in f:
          line = line.strip() # overwrite line bec line endings not needed
          if line.count(":") > 0:
             destination.append(line)
   logger.info(destination)
   expected_destination=['Italy: Rome', 'Greece: Athens', 'England: London, Manchester', 'France: Paris, Nice, Lyon', 'Spain: Madrid, Barcelona, Granada', 'Austria: Vienna']
   assert expected_destination == destination

def test_1014_3():
   ''' 10.14 Exercises Q3
   Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.
   '''
   j_emotions=[]
   with open("../data/emotion_words2.txt", "r") as f:
       for line in f:
          line = line.strip().lower() # overwrite line bec line endings not needed
          emotions = line.split(" ")
          for emotion in emotions:
             if emotion.startswith("j"):
                j_emotions.append(emotion)
   logger.info(j_emotions)
   expected_j = ['joyous', 'jittery', 'jumpy']
   assert expected_j == j_emotions

def test_1015_2():
   ''' 10.15 Exercise 2
   We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
   Find the total number of words in the file and assign this value to the variable num_words.
   '''
   with open("../data/emotion_words2.txt", "r") as f:
      rawString = f.read()
      num_chars = len(rawString)
      num_lines = rawString.count("\n")
      rawString = rawString.strip()
      words = rawString.replace("\n", " ").split(" ")
      num_words = len(words)
      logger.info("{} {} {}".format(num_chars, num_words, num_lines))
      assert (380, 48, 7) == (num_chars, num_words, num_lines)

def test_1015_5():
   '''  Using the file school_prompt.txt, assign the third word of every line to a list called three.
   '''
   three=[]
   with open("../data/school_prompt2.txt", "r") as f:
       for line in f:
           line = line.strip()
           words = line.split(" ")
           three.append(words[2])
       logger.info(three)
       expected = ['for', 'find', 'to', 'many', 'they', 'solid', 'for', 'have', 'some', 'ups,']
       assert expected == three

def test_1015_6():
   ''' Create a list called emotions that contains the first word of every line in emotion_words.txt.
   '''
   emotions=[]
   with open("../data/emotion_words2.txt", "r") as f:
       for line in f:
           line = line.strip()
           words = line.split(" ")
           emotions.append(words[0])
       logger.info(emotions)
       expected = ['Sad', 'Angry', 'Happy', 'Confused', 'Excited', 'Scared', 'Nervous']
       assert expected == emotions

def test_1015_9():
    ''' 10.5 Chapter Assessment Q9
        Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices 
        as well as some other financial indicators, including the “Long Term Interest Rate”, 
        which is interest rate paid on 10-year U.S. government bonds.
        Write a program that computes the average closing price (the second column, labeled SP500) 
        and the highest long-term interest rate. 
        Both should be computed only for the period from June 2016 through May 2017. 
        Save the results in the variables mean_SP and max_interest.
        Assumptions:
        1) Data is sorted by date
    '''
    sum_SP=0.0
    num_SP=0
    max_interest=0.0
    with open("../data/SP500.txt", "r") as f:
        for line in f:
           line = line.strip()
           (sdate, ssp500, dividend, earnings, cpi, sinterest, rprice, rdividend, rearninings, pe) = line.split(",") # s prefix for string
           # logger.info("{}: {} {}".format(sdate, ssp500, sinterest))
           if(sdate != "Date"): # skip header
               (smth, sday, syear) = sdate.split("/")
               mth=int(smth)
               year=int(syear)
               # logger.info("mth: {} year:{} s&p:{}".format(mth, year, ssp500))
               if((mth > 5 and year == 2016) or (mth < 6 and year == 2017)): # tricky logic
                   logger.info("mth:{} year:{} s&p:{}".format(mth, year,ssp500))
                   interest=float(sinterest)
                   sp500=float(ssp500)
                   if(interest > max_interest):
                       max_interest = interest
                   sum_SP += sp500
                   num_SP += 1
        mean_SP = sum_SP/num_SP
        logger.info("mean: {}, max:{} num:{}".format(mean_SP, max_interest, num_SP))
        assert math.isclose(2236.88166666, mean_SP)
        assert math.isclose(2.49, max_interest)


# endregion tests
