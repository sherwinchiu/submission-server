#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week1-question7.py
# Cashier, Advanced
# Week 1, Question 7

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "0.5 5 1 10")
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test1_text)[0]
    return float(num) == 12.5

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "0.732 15 1.58 25")
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test2_text)[0]
    return float(num) == 50.48   

def test3():
    rand1 = random.uniform(0, 5)
    rand2 = random.randint(0, 20)
    rand3 = random.uniform(0, 5)
    rand4 = random.randint(0, 20)
    test3_result = abs(rand1 * rand2 + rand3 * rand4)
    test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2) + " " + str(rand3) + " " + str(rand4)))
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test3_text)[0]
    return abs(float(num)) > test3_result*0.95 and abs(float(num)) < test3_result*1.05

def test4():
    rand1 = random.uniform(0, 100)
    rand2 = random.randint(0, 200)
    rand3 = random.uniform(0, 100)
    rand4 = random.randint(0, 200)
    test4_result = abs(rand1 * rand2 + rand3 * rand4)
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2) + " " + str(rand3) + " " + str(rand4)))
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test4_text)[0]
    return abs(float(num)) > test4_result*0.95 and abs(float(num)) < test4_result*1.05

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()    
except:
    sys.exit(1)
# Output results

test_outcome = [test1(), test2(), test3(), test4(), test4()]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)