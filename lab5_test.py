"""
author kvin
date 04112022
testing 4lab5
"""

from lab5 import *

def test_near_hundred():
    # Test below 100 True
    assert near_hundred(95) == True
    assert near_hundred(91) == True
    assert near_hundred(90) == True

    # Test below 100 False
    assert near_hundred(89) == False
    assert near_hundred(50) == False   

    # Test above 100 True
    assert near_hundred(105) == True
    assert near_hundred(109) == True
    assert near_hundred(110) == True
    
    # Test above 100 False
    assert near_hundred(111) == False
    assert near_hundred(150) == False

    # Test below 200 True
    assert near_hundred(195) == True
    assert near_hundred(191) == True
    assert near_hundred(190) == True

    # Test below 200 False
    assert near_hundred(189) == False
    assert near_hundred(149) == False   

    # Test above 200 True
    assert near_hundred(205) == True
    assert near_hundred(209) == True
    assert near_hundred(210) == True
    
    # Test above 200 False
    assert near_hundred(211) == False
    assert near_hundred(250) == False

def test_makes_ten(n):
    # Actually makes 10
    assert makes_ten(5,5) == True
    assert makes_ten(25,-15) == True

    # Does not make 10 but one number is 10
    assert makes_ten(100,10) == True
    assert makes_ten(10,-10) == True
    
    # Does not make 10 and no number is 10
    assert makes_ten(9,2) == False
    assert makes_ten(16,-5) == False

def test_front_back(s):
    # Normal tests


    assert front_back("computer") == "romputec"
    assert front_back("Science") == "eciencS"
    assert front_back("kayak") == "kayak"

    # Corner case one letter
    assert front_back("I") == "I"

    # Corner case two letters same
    assert front_back("ee") == "ee"

    # Corner case two letters different
    assert front_back("Be") == "eB"

def test_array_count9(arr):
    # Normal tests
    array_count9([1, 2, 3, 9, 3, 4, 9]) == 2
    array_count9([range(10)]) == 1
    array_count9([1, 2, 3, 4]) == 0

    # Corner case - Empty array
    array_count9([]) == 0

def test_get_magic_number(s):
    assert get_magic_number("one") == "three"
    assert get_magic_number("two") == "three"
    assert get_magic_number("three") == "four"
    assert get_magic_number("four") == "four"
    assert get_magic_number("five") == "four"
    assert get_magic_number("ninteen") == "seven"
    assert get_magic_number("twenty") == "six"


