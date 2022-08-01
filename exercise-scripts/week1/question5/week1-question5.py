#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week1-question5.py
# Double Variables
# Week 1, Question 5

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1(text):
    re_expressions = [r"cin\s*>>\s*\w+\s*;", r"cin\s*>>\s*\w+\s*>>\s*\w+\s*>>\s*\w+\s*;"]
    return (len(re.findall(re_expressions[0], text)) == 3 or bool(re.search(re_expressions[1], text)))

def test2(text):
    re_expressions = [r"double\s+\w+\s*", r"double\s+\w+\s*,\s*\w+\s*,\s*\w+"]
    return (len(re.findall(re_expressions[0], text)) >= 2 or bool(re.search(re_expressions[1], text)))

def test3(text):
    return bool(re.search(r"\w+\s*\+\s*\w+\s*\+\s*\w+\s*", text))

def test4():
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "5.5 10.5 2.5")
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test4_text)[0]
    return float(num) == 18.5

def test5():
    rand1 = random.uniform(-100, 100)
    rand2 = random.uniform(-100, 100)
    rand3 = random.uniform(-100, 100)
    test5_sum = abs(rand1 + rand2 + rand3)
    test5_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2) + " " + str(rand3)))
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test5_text)[0]
    return abs(float(num)) > test5_sum*0.95 and abs(float(num)) < test5_sum*1.05

def test6():
    rand1 = random.uniform(-10000, 10000)
    rand2 = random.uniform(-10000, 10000)
    rand3 = random.uniform(-10000, 10000)
    test6_sum = abs(rand1 + rand2 + rand3)
    test6_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2) + " " + str(rand3)))
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test6_text)[0]
    return abs(float(num)) > test6_sum*0.95 and abs(float(num)) < test6_sum*1.05

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()    
except:
    sys.exit(1)
# Output results

test_outcome = [test1(file_text), test2(file_text), test3(file_text), test4(), test5(), test6()]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)