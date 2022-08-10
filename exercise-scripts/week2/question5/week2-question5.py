#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question5
# Divisibility
# Week 2, Question 5

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1(text):
    return re.search(r"%", text, re.I)  

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "5 2")
    return re.search(r"is\s*not\s*divisible", test2_text, re.I)

def test3():
    test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "33 11")
    return re.search(r"is\s*divisible", test3_text, re.I)

def test4():
    rand1 = random.randint(1, 1000)
    rand2 = random.randint(1, 1000)
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], str(rand1) + " " + str(rand2))
    if (rand1 % rand2 == 0):
        return re.search(r"is\s*divisible", test4_text, re.I)
    else:
        return re.search(r"is\s*not\s*divisible", test4_text, re.I) 

def test5():
    result = True
    for i in range(1, 100):
        rand1 = random.randint(1, 1000)
        rand2 = random.randint(1, 1000)
        test5_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], str(rand1) + " " + str(rand2))
        if (rand1 % rand2 == 0):
            if (not re.search(r"is\s*divisible", test5_text, re.I)):
                result = False
        else:
            if (not re.search(r"is\s*not\s*divisible", test5_text, re.I)):
                result = False
        # idk the if statement values
    return result

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()    
except:
    sys.exit(1)
# Output results
test_outcome = [test1(file_text), test2(), test3(), test4(), test5()]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)