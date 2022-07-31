#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question1
# Number Comparison
# Week 2, Question 1

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "5 2")
    return re.search(r"5\s*is\s*greater\s*than\s*2", test1_text, re.I)

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3 3")
    return re.search(r"3\s*is\s*equal\s*to\s*3", test2_text, re.I)  
def test3():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "15 1")
    return re.search(r"15\s*is\s*less\s*than\s*1", test2_text, re.I)

def test4():
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0, 100)
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2)))
    if(rand1 < rand2):
        return re.search(str(rand1) + "\s*is\s*less\s*than\s*" + str(rand2), test4_text, re.I)
    elif(rand1 == rand2):
        return re.search(str(rand1) + "\s*is\s*equal\s*to\s*" + str(rand2), test4_text, re.I)
    else:
         return re.search(str(rand1) + "\s*is\s*less\s*than\s*" + str(rand2), test4_text, re.I)

def test5():
    rand1 = random.randint(0, 1000)
    rand2 = random.randint(0, 1000)
    test5_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2)))
    if(rand1 < rand2):
        return re.search(str(rand1) + "\s*is\s*less\s*than\s*" + str(rand2), test5_text, re.I)
    elif(rand1 == rand2):
        return re.search(str(rand1) + "\s*is\s*equal\s*to\s*" + str(rand2), test5_text, re.I)
    else:
        return re.search(str(rand1) + "\s*is\s*less\s*than\s*" + str(rand2), test5_text, re.I)

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