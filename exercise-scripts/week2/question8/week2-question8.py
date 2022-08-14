#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question8
# Reverse a Number
# Week 2, Question 8

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests

def reverse_num(input):
    string_input = ""
    while(input > 1):
        string_input += str(int(input%10))
        input /= 10
    return string_input

def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "10")
    return re.search(r"1", test1_text, re.I)  

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "12345")
    return re.search(r"54321", test2_text, re.I)

def test3():
    test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "5123514")
    return re.search(r"4153215", test3_text, re.I)

def test4():
    result = True
    for i in range(1, 100):
        rand1 = random.randint(1, 1000000)
        answer = reverse_num(rand1)
        test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], str(rand1))
        if (not re.search(str(answer), test4_text, re.I)):
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