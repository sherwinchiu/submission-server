#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question2
# Calculator
# Week 2, Question 2

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3 5 *")
    return re.search(r"15", test1_text)  

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3 5 +")
    return re.search(r"8", test2_text)

def test3():
    test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3 5 -")
    return re.search(r"-2", test3_text)

def test4():
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "3 5 /")
    return re.search(r"0.6", test4_text)

def test5(lower, upper):
    rand1 = random.uniform(lower, upper)
    rand2 = random.uniform(lower, upper)
    rand3 = random.randint(0, 3)
    answer = 0
    operation = ['+', '-', '*', '/']
    test5_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], (str(rand1) + " " + str(rand2) + " " +operation[rand3]))
    if(operation[rand3] == '+'):
        answer = rand1 + rand2
    elif(operation[rand3] == '-'):
        answer = rand1 - rand2
    elif(operation[rand3] == '*'):
        answer = rand1 * rand2
    else:
        answer = rand1 / rand2
    num = re.findall(r"-?[0-9]+\.?[0-9]*", test5_text)[0]
    return abs(float(num)) > abs(answer*0.99) and abs(float(num)) < abs(answer*1.01)

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()    
except:
    sys.exit(1)
# Output results
test_outcome = [test1(), test2(), test3(), test4(), test5(-100, 100), test5(-1000, 1000), test5(-1000, 1000)]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)