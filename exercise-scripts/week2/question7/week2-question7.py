#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question7
# Factorial
# Week 2, Question 7

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests

def factorial(input):
    answer = 1
    for i in range(1, input+1):
        answer *= i 
    return answer

def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "5")
    return re.search(r"120", test1_text, re.I)  

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3")
    return re.search(r"6", test2_text, re.I)

def test3():
    result = True
    for i in range(1, 100):
        rand1 = random.randint(1, 10)
        answer = factorial(rand1)
        test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], str(rand1))
        if (not re.search(str(answer), test3_text, re.I)):
            result = False
    return result

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()    
except:
    sys.exit(1)
# Output results
test_outcome = [test1(), test2(), test3()]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)