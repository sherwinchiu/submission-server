#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question8
# Rectangle
# Week 2, Question 9

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests

def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "5 4")
    return len(re.findall(r"\*{5}", test1_text, re.I)) == 4

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "1 1")
    return re.search(r"\*", test2_text, re.I)

def test3():
    test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3 3")
    return len(re.findall(r"\*{3}", test3_text, re.I)) == 3

def test4():
    result = True
    for i in range(1, 100):
        rand1 = random.randint(1, 100)
        rand2 = random.randint(1, 100)
        test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], str(rand1) + " " + str(rand2))
        if (not len(re.findall(r"\*{"+str(rand1)+"}", test4_text, re.I)) == rand2):
            result = False
    return result

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()    
except:
    sys.exit(1)
# Output results
test_outcome = [test1(), test2(), test3(), test4()]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)