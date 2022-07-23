#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week1-question8.py
# Change Calculator
# Week 1, Question 8

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "1 1 1 1 1")
    return float(test1_text) == 3.4

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "2 2 2 2 2")
    return float(test2_text) == 6.8   
def test3():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3 2 5 3 1")
    return float(test2_text) == 6.6

def test4():
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0, 100)
    rand3 = random.randint(0, 100)
    rand4 = random.randint(0, 100)
    rand5 = random.randint(0, 100)
    test4_result = abs(rand1*0.05 + rand2*0.1 + rand3*0.25 + rand4 + rand5*2)
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2) + " " + str(rand3) + " " + str(rand4) + " " + str(rand5)))
    return abs(float(test4_text)) > test4_result*0.99 and abs(float(test4_text)) < test4_result*1.01

def test5():
    rand1 = random.randint(0, 1000)
    rand2 = random.randint(0, 1000)
    rand3 = random.randint(0, 1000)
    rand4 = random.randint(0, 1000)
    rand5 = random.randint(0, 1000)
    test5_result = abs(rand1*0.05 + rand2*0.1 + rand3*0.25 + rand4 + rand5*2)
    test5_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2) + " " + str(rand3) + " " + str(rand4) + " " + str(rand5)))
    return abs(float(test5_text)) > test5_result*0.99 and abs(float(test5_text)) < test5_result*1.01

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