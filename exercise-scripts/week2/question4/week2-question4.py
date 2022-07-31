#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question4
# Working with ASCII
# Week 2, Question 4

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "?")
    return re.search(r"special", test1_text, re.I)  

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "5")
    return re.search(r"number", test2_text, re.I)

def test3():
    test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "A")
    return re.search(r"uppercase", test3_text, re.I)

def test4():
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "c")
    return re.search(r"lowercase", test4_text, re.I)

def test5():
    result = True
    for i in range(33, 126):
        test5_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], str(i))
        if(i >= 48 and i <= 57):
            if (not re.search(r"number", test5_text, re.I)):
                result = False
        elif(i >= 65 and i <= 90):
            if (not re.search(r"uppercase", test5_text, re.I)):
                result = False
        elif(i >= 97 and i <= 122):
            if (not re.search(r"lowercase", test5_text, re.I)):
                result = False
        else:
            if (not re.search(r"special", test5_text, re.I)):
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
test_outcome = [test1(), test2(), test3(), test4(), test5()]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)